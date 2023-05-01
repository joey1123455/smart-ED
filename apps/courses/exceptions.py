from rest_framework.exceptions import APIException


class CourseNotFound(APIException):
    status_code = 400
    default_detail = 'This course can not be found, it might have been deleted or was never uploaded'


class CourseUpdateNotPermitted(APIException):
    status_code = 403
    default_detail = 'You do not have permission to update this course'