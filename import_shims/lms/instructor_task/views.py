from import_shims.warn import warn_deprecated_import

warn_deprecated_import('instructor_task.views', 'lms.djangoapps.instructor_task.views')

from lms.djangoapps.instructor_task.views import *
