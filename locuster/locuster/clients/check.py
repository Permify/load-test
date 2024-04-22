import sys
import grpc
import inspect
import time
import gevent
import random

import locuster.proto.base.v1.service_pb2 as pb

from locust import task, events, constant
from locust.contrib.fasthttp import FastHttpUser
from locust.runners import STATE_STOPPING, STATE_STOPPED, STATE_CLEANUP, WorkerRunner

from locuster.lib import GrpcUser
from locuster.config import ENDPOINT
from locuster.proto.base.v1.service_pb2_grpc import PermissionStub, TenancyStub


class GRPCPermifyCheck(GrpcUser):
    host = ENDPOINT
    wait_time = constant(0)
    stub_class = PermissionStub

    def on_start(self):
        """ on_start is called when a Locust start before any task is scheduled """
        pass

    def on_stop(self):
        """ on_stop is called when the TaskSet is stopping """
        pass

    @task
    # @stopwatch
    def check_request(self):
        request_type = random.choice([1, 2, 3])

        if request_type == 1:
            entity = {
                "type": "content",
                "id": str(random.randint(1, 364583))
            }
        elif request_type == 2:
            entity = {
                "type": "user",
                "id": str(random.randint(1, 52083))
            }
        else:
            entity = {
                "type": "interaction",
                "id": str(random.randint(1, 104167))
            }
        
        subject = {
            "type": "user",
            "id": str(random.randint(1, 52083))
        }


        response = self.stub.Check(
                    pb.PermissionCheckRequest(
                        tenant_id='t1',
                        metadata=pb.PermissionCheckRequestMetadata(
                            snap_token='7XMAAAAAAAA=',
                            depth=100,
                            schema_version="coj7t38si3b1ki8vttv0"
                        ),
                        entity=entity,
                        permission="view",
                        subject=subject
                    )
                )
        print(response)