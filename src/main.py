from argparse import Namespace
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

from src.app.utils.parser_args import ParserArguments
from src.app.service.bussines.file_reader import CsvReader
from src.app.service.bussines.create_report import CreateReport


def create_report():
    ParserArguments.add_args()
    args: Namespace = ParserArguments.get_args_and_value()

    csv_reader = CsvReader(files=args.files, criteria=args.report)
    persons_info = csv_reader.processing_all_information()
    
    create_report = CreateReport(persons_info=persons_info)
    info_for_dispaly: list[tuple] = create_report.computing_performance(
        criteria=args.report
    )
    return create_report.display(data=info_for_dispaly)
    


if __name__ == "__main__":
    print(create_report())
