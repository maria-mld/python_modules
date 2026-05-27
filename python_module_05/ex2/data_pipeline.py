from abc import ABC, abstractmethod
from typing import Any, Union, List, Dict, Tuple, Protocol


class DataProcessor(ABC):
    def __init__(self) -> None:
        self._storage: List[Tuple[int, str]] = []
        self._counter: int = 0
        self.name: str = self.__class__.__name__

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> Tuple[int, str]:
        if not self._storage:
            raise IndexError("No data available in the processor")
        return self._storage.pop(0)

    @property
    def remaining(self) -> int:
        return len(self._storage)

    @property
    def total_processed(self) -> int:
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


class ExportPlugin(Protocol):
    def process_output(self, data: List[Tuple[int, str]]) -> None:
        ...


class CSVExportPlugin:
    def process_output(self, data: List[Tuple[int, str]]) -> None:
        if not data:
            return
        csv_string = ",".join(val for _, val in data)
        print("CSV Output:")
        print(csv_string)


class JSONExportPlugin:
    def process_output(self, data: List[Tuple[int, str]]) -> None:
        if not data:
            return
        pairs = [f'"item_{rank}": "{val}"' for rank, val in data]
        json_string = "{" + ", ".join(pairs) + "}"
        print("JSON Output:")
        print(json_string)


class DataStream:
    def __init__(self) -> None:
        self._processors: List[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        self._processors.append(proc)

    def process_stream(self, stream: List[Any]) -> None:
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

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        for processor in self._processors:
            collected_data: List[Tuple[int, str]] = []
            for _ in range(nb):
                try:
                    item = processor.output()
                    collected_data.append(item)
                except IndexError:
                    break
            if collected_data:
                plugin.process_output(collected_data)

    def print_processors_stats(self) -> None:
        print("== DataStream statistics ==")
        if not self._processors:
            print("No processor found, no data")
            return

        for proc in self._processors:
            friendly_name = proc.name.replace("Processor", " Processor")
            print(
                f"{friendly_name}: total {proc.total_processed} items "
                f"processed, remaining {proc.remaining} on processor"
            )


if __name__ == "__main__":
    print("=== Code Nexus - Data Pipeline ===")
    print("Initialize Data Stream...")
    pipeline = DataStream()
    pipeline.print_processors_stats()

    print("Registering Processors")
    num_proc = NumericProcessor()
    text_proc = TextProcessor()
    log_proc = LogProcessor()
    pipeline.register_processor(num_proc)
    pipeline.register_processor(text_proc)
    pipeline.register_processor(log_proc)

    batch_1 = [
        "Hello world",
        [3.14, -1, 2.71],
        [
            {"log_level": "WARNING",
             "log_message": "Telnet access! Use ssh instead"},
            {"log_level": "INFO", "log_message": "User wil is connected"}
        ],
        42,
        ["Hi", "five"]
    ]

    print("Send first batch of data on stream: ['Hello world', "
          "[3.14, -1, 2.71], [{'log_level': 'WARNING', 'log_message': "
          "'Telnet access! Use ssh instead'}, {'log_level': 'INFO', "
          "'log_message': 'User wil is connected'}], 42, ['Hi', 'five']]\n")

    pipeline.process_stream(batch_1)
    pipeline.print_processors_stats()

    print("\nSend 3 processed data from each processor to a CSV plugin:")
    csv_plugin = CSVExportPlugin()
    pipeline.output_pipeline(3, csv_plugin)
    pipeline.print_processors_stats()

    batch_2 = [
        21,
        ["I love AI", "LLMs are wonderful", "Stay healthy"],
        [
            {"log_level": "ERROR", "log_message": "500 server crash"},
            {"log_level": "NOTICE",
             "log_message": "Certificate expires in 10 days"}
        ],
        [32, 42, 64, 84, 128, 168],
        "World hello"
    ]

    print("\nSend another batch of data: [21, ['I love AI', "
          "'LLMs are wonderful', 'Stay healthy'], "
          "[{'log_level': 'ERROR', 'log_message': '500 server crash'}, "
          "{'log_level': 'NOTICE', 'log_message': "
          "'Certificate expires in 10 days'}], "
          "[32, 42, 64, 84, 128, 168], 'World hello']")

    pipeline.process_stream(batch_2)
    pipeline.print_processors_stats()

    print("\nSend 5 processed data from each processor to a JSON plugin:")
    json_plugin = JSONExportPlugin()
    pipeline.output_pipeline(5, json_plugin)
    pipeline.print_processors_stats()
