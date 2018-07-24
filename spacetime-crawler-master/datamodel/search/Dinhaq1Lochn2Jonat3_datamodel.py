'''
Created on Oct 20, 2016
@author: Rohan Achar
'''
from rtypes.pcc.attributes import dimension, primarykey, predicate
from rtypes.pcc.types.subset import subset
from rtypes.pcc.types.set import pcc_set
from rtypes.pcc.types.projection import projection
from rtypes.pcc.types.impure import impure
from datamodel.search.server_datamodel import Link, ServerCopy

@pcc_set
class Dinhaq1Lochn2Jonat3Link(Link):
    USERAGENTSTRING = "Dinhaq1Lochn2Jonat3"

    @dimension(str)
    def user_agent_string(self):
        return self.USERAGENTSTRING

    @user_agent_string.setter
    def user_agent_string(self, v):
        # TODO (rachar): Make it such that some dimensions do not need setters.
        pass


@subset(Dinhaq1Lochn2Jonat3Link)
class Dinhaq1Lochn2Jonat3UnprocessedLink(object):
    @predicate(Dinhaq1Lochn2Jonat3Link.download_complete, Dinhaq1Lochn2Jonat3Link.error_reason)
    def __predicate__(download_complete, error_reason):
        return not (download_complete or error_reason)


@impure
@subset(Dinhaq1Lochn2Jonat3UnprocessedLink)
class OneDinhaq1Lochn2Jonat3UnProcessedLink(Dinhaq1Lochn2Jonat3Link):
    __limit__ = 1

    @predicate(Dinhaq1Lochn2Jonat3Link.download_complete, Dinhaq1Lochn2Jonat3Link.error_reason)
    def __predicate__(download_complete, error_reason):
        return not (download_complete or error_reason)

@projection(Dinhaq1Lochn2Jonat3Link, Dinhaq1Lochn2Jonat3Link.url, Dinhaq1Lochn2Jonat3Link.download_complete)
class Dinhaq1Lochn2Jonat3ProjectionLink(object):
    pass
