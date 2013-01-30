from collective.grok import gs
from wcc.ewnpolicy import MessageFactory as _

@gs.importstep(
    name=u'wcc.ewnpolicy', 
    title=_('wcc.ewnpolicy import handler'),
    description=_(''))
def setupVarious(context):
    if context.readDataFile('wcc.ewnpolicy.marker.txt') is None:
        return
    portal = context.getSite()

    # do anything here
