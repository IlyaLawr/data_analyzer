from typing import Any

from pandas.core.frame import DataFrame

from RestrictedPython import compile_restricted, safe_globals
from RestrictedPython.Guards import guarded_iter_unpack_sequence, safer_getattr
from RestrictedPython.Eval import default_guarded_getiter, default_guarded_getitem


class ExecuteCodeService:
    def __init__(self) -> None:
        self._env = safe_globals.copy()
        self._env.update({
            '_getattr_': safer_getattr,
            '_getitem_': default_guarded_getitem,  
            '_getiter_': default_guarded_getiter,
            '_iter_unpack_sequence_': guarded_iter_unpack_sequence,
            'result': None})


    def execute(self, code: str, df: DataFrame) -> Any:
        self._env['df'] = df
        byte_code = compile_restricted(code, mode='exec')
        exec(byte_code, self._env)
        return self._env['result']
