from import_shims.warn import warn_deprecated_import

warn_deprecated_import('courseware.tests.test_middleware', 'lms.djangoapps.courseware.tests.test_middleware')

from lms.djangoapps.courseware.tests.test_middleware import *
