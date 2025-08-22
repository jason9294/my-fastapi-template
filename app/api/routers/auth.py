from fastapi import APIRouter

router = APIRouter(prefix='/auth', tags=['auth'])


@router.post(
    path='/login',
    summary='login',
)
async def login():
    return ...


@router.post(
    path='/refresh',
    summary='refresh',
)
async def refresh():
    return ...


@router.post(
    path='/logout',
    summary='logout',
)
async def logout():
    return ...


@router.post(
    path='/register',
    summary='register',
)
async def register():
    return ...
