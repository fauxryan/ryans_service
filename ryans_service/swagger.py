# -*- coding: utf-8 -*-
from apispec import APISpec

__all__ = ['spec']


spec = APISpec(
    title='ryans_service',
    version='0.1.0',
    info=dict(
        description='My new project'
    ),
    plugins=('apispec.ext.marshmallow',)
)


spec.add_path(
    path='/',
    operations=dict(
        get=dict(
            responses={
                '200': {
                    'schema': 'string'
                }
            }
        )
    )
)


spec.add_path(
    path='/health',
    description='Indicates the health of the application',
    operations=dict(
        get=dict(
            responses={
                '200': {
                    'schema': 'string'
                },
                '503': {
                    'schema': 'string',
                    'description': 'The application is not available'
                }
            }
        )
    )
)


spec.add_path(
    path='/status',
    description='Indicates the live status of the application',
    operations=dict(
        get=dict(
            responses={
                '200': {
                    'schema': 'string'
                }
            }
        )
    )
)