import re
import os

from constants.mismatchTypes import INVALID_KINDS
from constants.keywords import keywords
from constants.lexicalSpecs import lexical_specifications

tok_regex = '|'.join('(?P<%s>%s)' % pair for pair in lexical_specifications)


def tokenize(code):
    content = open(code, "r").read()
    line_counter = 1

    for match in re.finditer(tok_regex, content):
        kind = match.lastgroup
        value = match.group()
        if kind == 'id' and value in keywords:
            kind = value
        elif kind == 'SKIP':
            continue
        elif kind == 'NEWLINE':
            line_counter = line_counter + 1
            continue
        elif kind == 'blockcmt':
            line_counter = line_counter + value.count('\n')
        elif kind == 'MISMATCH':
            kind = get_kind_on_mismatch(value)
        elif kind == 'EOF':
            value = '$'
        elif kind == 'EPSILON':
            value = 'EPSILON'
        yield kind, value, line_counter


def get_kind_on_mismatch(value):
    invalid_char = {'@', '#', '$', '~', '\'', '\\'}
    if value in invalid_char:
        kind = INVALID_KINDS.INVALIDCHAR.value
    elif re.match(r'^0+[\d]\.?[\d]?|\d*\.\d*[0]$|\d*\.\d*[e|E][0]\d*[0]?$', value):
        kind = INVALID_KINDS.INVALIDNUM.value
    elif re.match(r'^_|^[0-9]|^_[0-9][a-zA-Z]\w*', value):
        kind = INVALID_KINDS.INVALIDID.value
    else:
        print('Could not decide the error type')
        kind = INVALID_KINDS.UNKNOWN.value
    return kind


if __name__ == '__main__':
    testsFolder = 'tests/'
    resultsFolder = 'results/'
    for test_file_name in os.listdir(testsFolder):
        with open(resultsFolder + test_file_name + ".outlexerrors", 'w') as error_file:
            with open(resultsFolder + test_file_name + ".outlextokens", 'w') as tokens_file:
                for token in tokenize(testsFolder + test_file_name):
                    if INVALID_KINDS.is_invalid(token[0]):
                        error_file.write(str(token))
                        error_file.write('\n')
                    else:
                        tokens_file.write(str(token))
                        tokens_file.write('\n')
                    print(token)
