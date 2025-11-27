from app.api import BaseRouter, DashRouter

router = BaseRouter(route_class=DashRouter)


@router.get('/')
async def get_example():
    return {'message': 'This is an example endpoint from API v2 with DashRouter.'}
