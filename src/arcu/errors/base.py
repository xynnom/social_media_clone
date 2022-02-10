from fastapi import HTTPException


class ItemNotFound(HTTPException):
    """Object not found.

    There are no existing objects.
    """
    def __init__(self, resource: str = 'Item'):
        super().__init__(status_code=404,
                         detail=f'{resource.capitalize()} not found.')


class ServerError(HTTPException):
    """Error on response being sent.

    The response being created does not follow the response_model.
    """
    status_code = 500
    detail = 'Internal Server Error.'

    def __init__(self):
        super().__init__(status_code=self.status_code, detail=self.detail)


class ActionNotAllowed(HTTPException):
    """Action is not permitted

    There are no entitlement entry for the current user.
    """
    status_code = 405
    detail = 'Not allowed to this action.'

    def __init__(self):
        super().__init__(status_code=self.status_code, detail=self.detail)


class AuthUnauthorized(HTTPException):
    """Error on unauthorized users

    This error is thrown when a user or an anonymous
    user accesses a protected endpoint
    """
    status_code = 403
    detail = 'No permission to access the endpoint.'

    def __init__(self):
        super().__init__(status_code=self.status_code, detail=self.detail)


class DuplicateItem(HTTPException):
    """Error on unauthorized users

    This error is thrown when a user or an anonymous
    user accesses a protected endpoint
    """
    status_code = 409
    detail = 'Object already exists.'

    def __init__(self):
        super().__init__(status_code=self.status_code, detail=self.detail)
