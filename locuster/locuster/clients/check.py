import sys
import grpc
import inspect
import time
import gevent

from locust import task, events, constant
from locust.contrib.fasthttp import FastHttpUser
from locust.runners import STATE_STOPPING, STATE_STOPPED, STATE_CLEANUP, WorkerRunner

from locuster.config import ENDPOINT
from locuster.proto.service_pb2_grpc import Permission, PermissionStub


def stopwatch(func):
    """To be updated"""

    def wrapper(*args, **kwargs):
        """To be updated"""
        # get task's function name
        previous_frame = inspect.currentframe().f_back
        _, _, task_name, _, _ = inspect.getframeinfo(previous_frame)

        start = time.time()
        result = None
        try:
            result = func(*args, **kwargs)
        except Exception as e:
            total = int((time.time() - start) * 1000)
            events.request_failure.fire(
                request_type="TYPE",
                name=task_name,
                response_time=total,
                response_length=0,
                exception=e
            )
        else:
            total = int((time.time() - start) * 1000)
            events.request_success.fire(
                request_type="TYPE",
                name=task_name,
                response_time=total,
                response_length=0
            )
        return result
    return wrapper


class GRPCMyLocust(FastHttpUser):
    wait_time = constant(0)

    def on_start(self):
        """ on_start is called when a Locust start before any task is scheduled """
        pass

    def on_stop(self):
        """ on_stop is called when the TaskSet is stopping """
        pass

    @task
    @stopwatch
    def grpc_client_task(self):
        """To be updated"""
        try:
            with grpc.insecure_channel(ENDPOINT) as channel:
                stub = None # todo
                response = None # todo
                print(response)
        except (KeyboardInterrupt, SystemExit):
            sys.exit(0)


# Stopping the locust if a threshold (in this case the fail ratio) is exceeded
def checker(environment):
    while not environment.runner.state in [STATE_STOPPING, STATE_STOPPED, STATE_CLEANUP]:
        time.sleep(1)
        if environment.runner.stats.total.fail_ratio > 0.2:
            print(f"fail ratio was {environment.runner.stats.total.fail_ratio}, quitting")
            environment.runner.quit()
            return


@events.init.add_listener
def on_locust_init(environment, **_kwargs):
    if not isinstance(environment.runner, WorkerRunner):
        gevent.spawn(checker, environment)