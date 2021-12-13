# test_tccm_api.py - Test whether the TCCM API works
import pytest

from sheet2linkml.terminologies.tccm.api import TCCMService


class TestTCCMService:
    def test_tccm_service(self):
        """Test case to check that the terminology service URL is being
        captured"""
        tccm = TCCMService("https://terminology.ccdh.io")
        assert tccm.base_url == "https://terminology.ccdh.io"

    def test_get_enum_values_for_field_failure(self):
        """Test case when field name does not exist in the model"""
        tccm = TCCMService("https://terminology.ccdh.io")

        assert tccm.get_enum_values_for_field("CRDC-H:Foo.bar") == {}

    def test_get_enum_values_for_field_enum_not_exist(self):
        """Test case for when field exists, but does not have an
        enumeration"""
        tccm = TCCMService("https://terminology.ccdh.io")

        assert tccm.get_enum_values_for_field("CRDC-H:CancerStageObservation.id") == {}

    @pytest.mark.skip("CCDH Terminology Serivce enumerations endpoint has been changed")
    def test_get_enum_values_for_field_enum_exists(self):
        """Test case for when field exists and has an enumeration"""
        tccm = TCCMService("https://terminology.ccdh.io")

        enum_result = tccm.get_enum_values_for_field("CRDC-H.Subject.cause_of_death")

        assert (
            enum_result["description"]
            == "Autogenerated Enumeration for CRDC-H Subject cause_of_death"
        )

        assert enum_result["permissible_values"] == {}