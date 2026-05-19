from abc import ABC, abstractmethod
from typing import Any, Union, List, Dict


class DataProcessor(ABC):
    def __init__(self) -> None:
        self._storage: List[tuple[int, str]] = []
        self._counter: int = 0
        # Добавляем имя класса для красивого вывода статистики
        self.name: str = self.__class__.__name__

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        if not self._storage:
            raise IndexError("No data available in the processor")
        return self._storage.pop(0)

    @property
    def remaining(self) -> int:
        """Возвращает количество элементов, оставшихся в буфере."""
        return len(self._storage)

    @property
    def total_processed(self) -> int:
        """Возвращает общее количество обработанных элементов."""
        return self._counter


class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, (int, float)):
            return not isinstance(data, bool)
        if isinstance(data, list):
            if not data:
                return True
            return all(
                isinstance(x, (int, float)) and not isinstance(x, bool)
                for x in data
            )
        return False

    def ingest(self, data: Union[int, float, List[Union[int, float]]]) -> None:
        if not self.validate(data):
            raise ValueError("Improper numeric data")

        if isinstance(data, list):
            for item in data:
                self._storage.append((self._counter, str(item)))
                self._counter += 1
        else:
            self._storage.append((self._counter, str(data)))
            self._counter += 1


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            return True
        if isinstance(data, list):
            return all(isinstance(x, str) for x in data)
        return False

    def ingest(self, data: Union[str, List[str]]) -> None:
        if not self.validate(data):
            raise ValueError("Improper text data")

        if isinstance(data, list):
            for item in data:
                self._storage.append((self._counter, item))
                self._counter += 1
        else:
            self._storage.append((self._counter, data))
            self._counter += 1


class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        def is_valid_log(d: Any) -> bool:
            if not isinstance(d, dict):
                return False
            return all(
                isinstance(k, str) and isinstance(v, str) for k, v in d.items()
            )

        if isinstance(data, dict):
            return is_valid_log(data)
        if isinstance(data, list):
            return all(is_valid_log(x) for x in data)
        return False

    def ingest(self, data: Union[Dict[str, str],
                                 List[Dict[str, str]]]) -> None:
        if not self.validate(data):
            raise ValueError("Improper log data")

        def format_log(d: Dict[str, str]) -> str:
            level = d.get("log_level", "")
            message = d.get("log_message", "")
            return f"{level}: {message}"

        if isinstance(data, list):
            for item in data:
                self._storage.append((self._counter, format_log(item)))
                self._counter += 1
        else:
            self._storage.append((self._counter, format_log(data)))
            self._counter += 1


class DataStream:
    """Управляющий класс потока данных."""

    def __init__(self) -> None:
        self._processors: List[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        """Регистрирует новый процессор в системе."""
        self._processors.append(proc)

    def process_stream(self, stream: list[Any]) -> None:
        """Анализирует каждый элемент и отправляет его в нужный процессор."""
        for element in stream:
            handled = False
            for processor in self._processors:
                if processor.validate(element):
                    processor.ingest(element)
                    handled = True
                    break
            if not handled:
                print(
                    f"DataStream error - Can't process element in stream: "
                    f"{element}"
                )

    def print_processors_stats(self) -> None:

        print("== DataStream statistics ==")
        if not self._processors:
            print("No processor found, no data")
            return

        for proc in self._processors:
            # Превращаем имя 'NumericProcessor' в красивое 'Numeric Processor'
            friendly_name = proc.name.replace("Processor", "Processor")
            # Добавим пробел перед словом Processor для соответствия ТЗ
            if "Numeric" in friendly_name:
                friendly_name = "Numeric Processor"
            elif "Text" in friendly_name:
                friendly_name = "Text Processor"
            elif "Log" in friendly_name:
                friendly_name = "Log Processor"

            print(
                f"{friendly_name}: total {proc.total_processed} items "
                f"processed, remaining {proc.remaining} on processor"
            )


# --- Тестовый сценарий по ТЗ ---
if __name__ == "__main__":
    print("=== Code Nexus - Data Stream ===")
    print("Initialize Data Stream...")
    stream_manager = DataStream()
    stream_manager.print_processors_stats()

    print("Registering Numeric Processor")
    num_processor = NumericProcessor()
    stream_manager.register_processor(num_processor)

    # Наш батч данных из примера
    batch = [
        "Hello world",
        [3.14, -1, 2.71],
        [
            {
                "log_level": "WARNING",
                "log_message": "Telnet access! Use ssh instead",
            },
            {"log_level": "INFO", "log_message": "User wil is connected"},
        ],
        42,
        ["Hi", "five"],
    ]

    print("Send first batch of data on stream: "
          "['Hello world', [3.14, -1, 2.71], [{'log_level': 'WARNING', "
          "'log_message': 'Telnet access! Use ssh instead'}, "
          "{'log_level': 'INFO', 'log_message': 'User wil is connected'}], "
          "42, ['Hi', 'five']]\n")

    stream_manager.process_stream(batch)
    stream_manager.print_processors_stats()

    print("Registering other data processors")
    text_processor = TextProcessor()
    log_processor = LogProcessor()
    stream_manager.register_processor(text_processor)
    stream_manager.register_processor(log_processor)

    print("Send the same batch again")
    stream_manager.process_stream(batch)
    stream_manager.print_processors_stats()

    print("Consume some elements from the data processors: "
          "Numeric 3, Text 2, Log 1")
    # Извлекаем элементы
    for _ in range(3):
        num_processor.output()
    for _ in range(2):
        text_processor.output()
    for _ in range(1):
        log_processor.output()

    stream_manager.print_processors_stats()
