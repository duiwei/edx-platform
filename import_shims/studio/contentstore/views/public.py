from import_shims.warn import warn_deprecated_import

warn_deprecated_import('contentstore.views.public', 'cms.djangoapps.contentstore.views.public')

from cms.djangoapps.contentstore.views.public import *
