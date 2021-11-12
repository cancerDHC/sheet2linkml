# test_tccm_api.py - Test whether the TCCM API works

from sheet2linkml.terminologies.tccm.api import TCCMService


def test_tccm_service():
    tccm = TCCMService('https://terminology.ccdh.io')
    assert tccm.base_url == 'https://terminology.ccdh.io'
