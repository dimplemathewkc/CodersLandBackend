from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_http_methods
import json
from utils import RunCode
from loguru import logger


@require_http_methods(["POST"])
def compile_python(request):
    #todo what to do about functions??
    payload = json.loads(request.body.decode('utf-8'))
    logger.debug(payload)
    code = payload.get("code")
    print(code)
    run = RunCode(code)
    rescompile, resrun = run.run_code()
    logger.info(rescompile,resrun)
    if resrun == "" and rescompile == "":
        status = f'Code Execution Successful😀  "\n \t"'\
                 'Hint: call function in main \n' \
                 'if __name__ == "__main__": \n' \
                 '  function()'
    elif resrun == "" and rescompile != "":
        status = '-- Fail -- 😰'
    else:
        status = '-- Success -- 😀'
    return JsonResponse({"trace": rescompile,
                         "resrun" : resrun,
                         "status": status
                         })
