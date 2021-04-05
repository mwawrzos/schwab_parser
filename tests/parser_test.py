import datetime as d
import pytest

import schwab_parser.parsers as p
import schwab_parser.entries as e


def split_csv(txt):
    return [row.split(',') for row in txt.strip().splitlines()]


@pytest.fixture
def espp_deposit_lines():
    deposit_lines = '''
"Date","Action","Symbol","Description","Quantity","Fees & Commissions","Disbursement Election","Amount"
"2001/04/05","Deposit","AAPL","ESPP",42,"","",""
'''
    return split_csv(deposit_lines)

@pytest.fixture
def parser(espp_deposit_lines):
    header, *_ = espp_deposit_lines
    return p.Parser(header)

@pytest.fixture
def rows(espp_deposit_lines):
    return espp_deposit_lines[1:]

def test_wrong_header(espp_deposit_lines):
    header, *rows = espp_deposit_lines
    with pytest.raises(Exception, match='Header not supported'):
        p.Parser([])

def test_short_row(parser):
    with pytest.raises(Exception, match='Expected more than two columns'):
        parser.parse([])

def test_not_supported(parser, rows):
    row = rows[0]
    row[1] = 'not supported deposit'
    with pytest.raises(Exception, match='Not supported row'):
        parser.parse(row)

def test_espp_deposit(parser, rows):
    parser, _ = parser.parse(rows[0])

    assert isinstance(parser, p.DepositParser)

