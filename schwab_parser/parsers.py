
supported_headers = [
    [
        '"Date"',
        '"Action"',
        '"Symbol"',
        '"Description"',
        '"Quantity"',
        '"Fees & Commissions"',
        '"Disbursement Election"',
        '"Amount"',
    ]
]


class Parser:
    def __init__(self, header):
        if header not in supported_headers:
            raise Exception(
                f'Header not supported. Expected {supported_headers},'
                f' found {header}.'
            )
        self.header = header

    def parse(self, row):
        if len(row) < 2:
            raise Exception(
                f'Expected more than two columns. Found: {len(row)}'
            )
        if row[1] == '"Deposit"':
            return DepositParser(self.header, row), None
        raise Exception(f'Not supported row: {row}')


class DepositParser(Parser):
    def __init__(self, header, *args):
        super(DepositParser, self).__init__(header)
