class PhiKasException(Exception):
    """Base exception class for all PhiKas internal execution faults."""

class AuthenticationError(PhiKasException):
    """Raised when an incoming ingestion payload fails HMAC validation verification."""

class SLAViolationError(PhiKasException):
    """Raised when a system mutation crosses safe performance metric limits."""
