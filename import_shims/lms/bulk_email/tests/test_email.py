from import_shims.warn import warn_deprecated_import

warn_deprecated_import('bulk_email.tests.test_email', 'lms.djangoapps.bulk_email.tests.test_email')

from lms.djangoapps.bulk_email.tests.test_email import *
