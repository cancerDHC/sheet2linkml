# test_tccm_api.py - Test whether the TCCM API works
import pytest

from sheet2linkml.terminologies.tccm.api import TCCMService


class TestTCCMService:
    def test_tccm_service(self):
        tccm = TCCMService('https://terminology.ccdh.io')
        assert tccm.base_url == 'https://terminology.ccdh.io'

    @pytest.mark.skip("CCDH Terminology Service is down")
    def test_get_enum_values_for_field_failure(self):
        tccm = TCCMService('https://terminology.ccdh.io')

        assert tccm.get_enum_values_for_field("CRDC-H:Foo.bar") == {}

    def test_get_enum_values_for_field_enum_not_exist(self):
        tccm = TCCMService('https://terminology.ccdh.io')

        with pytest.raises(RuntimeError) as excinfo:
            tccm.get_enum_values_for_field("CRDC-H:CancerStageObservation.id")

        assert "Error accessing TCCM Terminology Service" in str(excinfo.value)
