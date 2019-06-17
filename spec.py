# -*- generated by 1.0.12 -*-
import da
PatternExpr_196 = da.pat.TuplePattern([da.pat.ConstantPattern('request'), da.pat.FreePattern('c2'), da.pat.FreePattern('p')])
PatternExpr_221 = da.pat.TuplePattern([da.pat.ConstantPattern('release'), da.pat.BoundPattern('_BoundPattern224_'), da.pat.BoundPattern('_BoundPattern225_')])
PatternExpr_254 = da.pat.TuplePattern([da.pat.ConstantPattern('ack'), da.pat.BoundPattern('_BoundPattern257_'), da.pat.BoundPattern('_BoundPattern258_')])
PatternExpr_300 = da.pat.TuplePattern([da.pat.ConstantPattern('request'), da.pat.FreePattern('c'), da.pat.FreePattern('p')])
PatternExpr_367 = da.pat.TuplePattern([da.pat.ConstantPattern('done')])
PatternExpr_372 = da.pat.BoundPattern('_BoundPattern374_')
PatternExpr_375 = da.pat.TuplePattern([da.pat.FreePattern(None), da.pat.TuplePattern([da.pat.FreePattern(None), da.pat.FreePattern(None), da.pat.BoundPattern('_BoundPattern381_')]), da.pat.TuplePattern([da.pat.ConstantPattern('done')])])
PatternExpr_228 = da.pat.TuplePattern([da.pat.FreePattern(None), da.pat.TuplePattern([da.pat.FreePattern(None), da.pat.FreePattern(None), da.pat.FreePattern(None)]), da.pat.TuplePattern([da.pat.ConstantPattern('release'), da.pat.BoundPattern('_BoundPattern238_'), da.pat.BoundPattern('_BoundPattern239_')])])
PatternExpr_261 = da.pat.TuplePattern([da.pat.FreePattern(None), da.pat.TuplePattern([da.pat.FreePattern(None), da.pat.FreePattern(None), da.pat.FreePattern(None)]), da.pat.TuplePattern([da.pat.ConstantPattern('ack'), da.pat.BoundPattern('_BoundPattern271_'), da.pat.BoundPattern('_BoundPattern272_')])])
_config_object = {'channel': 'fifo', 'clock': 'Lamport'}
import sys
import time

class P(da.DistProcess):

    def __init__(self, procimpl, props):
        super().__init__(procimpl, props)
        self._PReceivedEvent_0 = []
        self._PReceivedEvent_1 = []
        self._PReceivedEvent_2 = []
        self._PReceivedEvent_4 = []
        self._events.extend([da.pat.EventPattern(da.pat.ReceivedEvent, '_PReceivedEvent_0', PatternExpr_196, sources=None, destinations=None, timestamps=None, record_history=True, handlers=[]), da.pat.EventPattern(da.pat.ReceivedEvent, '_PReceivedEvent_1', PatternExpr_221, sources=None, destinations=None, timestamps=None, record_history=True, handlers=[]), da.pat.EventPattern(da.pat.ReceivedEvent, '_PReceivedEvent_2', PatternExpr_254, sources=None, destinations=None, timestamps=None, record_history=True, handlers=[]), da.pat.EventPattern(da.pat.ReceivedEvent, '_PReceivedEvent_3', PatternExpr_300, sources=None, destinations=None, timestamps=None, record_history=None, handlers=[self._P_handler_299]), da.pat.EventPattern(da.pat.ReceivedEvent, '_PReceivedEvent_4', PatternExpr_367, sources=[PatternExpr_372], destinations=None, timestamps=None, record_history=True, handlers=[])])

    def setup(self, s, nrequests, logps, **rest_386):
        super().setup(s=s, nrequests=nrequests, logps=logps, **rest_386)
        self._state.s = s
        self._state.nrequests = nrequests
        self._state.logps = logps
        pass

    def run(self):
        start_cpu_time = time.time()

        def task():
            pass
        for i in range(self._state.nrequests):
            self.mutex(task)
        self.send(('done', self._id), to=self.parent())
        end_cpu_time = time.time()
        total_cpu_time = (end_cpu_time - start_cpu_time)
        self.send(('cputime', total_cpu_time, self._id), to=self._state.logps)
        super()._label('_st_label_364', block=False)
        _st_label_364 = 0
        while (_st_label_364 == 0):
            _st_label_364 += 1
            if PatternExpr_375.match_iter(self._PReceivedEvent_4, _BoundPattern381_=self.parent(), SELF_ID=self._id):
                _st_label_364 += 1
            else:
                super()._label('_st_label_364', block=True)
                _st_label_364 -= 1

    def mutex(self, task):
        super()._label('request', block=False)
        c = self.logical_clock()
        self.send(('request', c, self._id), to=self._state.s)
        super()._label('_st_label_192', block=False)
        p = c2 = None

        def UniversalOpExpr_194():
            nonlocal p, c2
            for (_, _, (_ConstantPattern213_, c2, p)) in self._PReceivedEvent_0:
                if (_ConstantPattern213_ == 'request'):
                    if (not (PatternExpr_228.match_iter(self._PReceivedEvent_1, _BoundPattern238_=c2, _BoundPattern239_=p, SELF_ID=self._id) or ((c, self._id) < (c2, p)))):
                        return False
            return True
        p = None

        def UniversalOpExpr_247():
            nonlocal p
            for p in self._state.s:
                if (not PatternExpr_261.match_iter(self._PReceivedEvent_2, _BoundPattern271_=c, _BoundPattern272_=p, SELF_ID=self._id)):
                    return False
            return True
        _st_label_192 = 0
        while (_st_label_192 == 0):
            _st_label_192 += 1
            if (UniversalOpExpr_194() and UniversalOpExpr_247()):
                _st_label_192 += 1
            else:
                super()._label('_st_label_192', block=True)
                _st_label_192 -= 1
        super()._label('critical_section', block=False)
        self.send(('incs', self.logical_clock(), self._id), to=self._state.logps)
        task()
        self.send(('outcs', self.logical_clock(), self._id), to=self._state.logps)
        super()._label('release', block=False)
        self.send(('release', c, self._id), to=self._state.s)

    def _P_handler_299(self, c, p):
        self.send(('ack', c, self._id), to=p)
    _P_handler_299._labels = None
    _P_handler_299._notlabels = None