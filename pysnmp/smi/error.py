#
# This file is part of pysnmp software.
#
# Copyright (c) 2005-2020, Ilya Etingof <etingof@gmail.com>
# License: https://www.pysnmp.com/pysnmp/license.html
#
from pyasn1.error import PyAsn1Error
from pysnmp.error import PySnmpError


class SmiError(PySnmpError, PyAsn1Error):
    pass


class MibLoadError(SmiError):
    pass


class MibNotFoundError(MibLoadError):
    pass


class MibOperationError(SmiError):
    def __init__(self, **kwargs):
        self.__outArgs = kwargs

    def __str__(self):
        return f"{self.__class__.__name__}({self.__outArgs})"

    def __getitem__(self, key):
        return self.__outArgs[key]

    def __contains__(self, key):
        return key in self.__outArgs

    def get(self, key, defVal=None):
        return self.__outArgs.get(key, defVal)

    def keys(self):
        return self.__outArgs.keys()

    def update(self, d):
        self.__outArgs.update(d)


# Aligned with SNMPv2 PDU error-status values


class TooBigError(MibOperationError):
    pass


class NoSuchNameError(MibOperationError):
    pass


class BadValueError(MibOperationError):
    pass


class ReadOnlyError(MibOperationError):
    pass


class GenError(MibOperationError):
    pass


class NoAccessError(MibOperationError):
    pass


class WrongTypeError(MibOperationError):
    pass


class WrongLengthError(MibOperationError):
    pass


class WrongEncodingError(MibOperationError):
    pass


class WrongValueError(MibOperationError):
    pass


class NoCreationError(MibOperationError):
    pass


class InconsistentValueError(MibOperationError):
    pass


class ResourceUnavailableError(MibOperationError):
    pass


class CommitFailedError(MibOperationError):
    pass


class UndoFailedError(MibOperationError):
    pass


class AuthorizationError(MibOperationError):
    pass


class NotWritableError(MibOperationError):
    pass


class InconsistentNameError(MibOperationError):
    pass


# Aligned with SNMPv2 PDU exceptions or error-status values


class NoSuchObjectError(NoSuchNameError):
    pass


class NoSuchInstanceError(NoSuchNameError):
    pass


class EndOfMibViewError(NoSuchNameError):
    pass


# SNMP table management exceptions


class TableRowManagement(MibOperationError):
    pass


class RowCreationWanted(TableRowManagement):
    pass


class RowDestructionWanted(TableRowManagement):
    pass
