# SPDX-FileCopyrightText: 2020 PANGAEA (https://www.pangaea.de/)
#
# SPDX-License-Identifier: MIT

from urllib.parse import urlparse

from fuji_server.evaluators.fair_evaluator import FAIREvaluator
from fuji_server.models.standardised_protocol_data import StandardisedProtocolData
from fuji_server.models.standardised_protocol_data_output import StandardisedProtocolDataOutput


class FAIREvaluatorStandardisedProtocolData(FAIREvaluator):
    """
    A class to evaluate whether the data is accessible through a standardized communication protocol (A1-03D).
    A child class of FAIREvaluator.
    ...

    Methods
    ------
    evaluate()
        This method will evaluate the accesibility of the data on whether the URI's scheme is based on
        a shared application protocol.
    """

    def __init__(self, fuji_instance):
        FAIREvaluator.__init__(self, fuji_instance)
        self.set_metric(["FsF-A1-03D", "FRSM-09-A1"])
        self.data_output = {}

    def testStandardProtocolDataUsed(self):
        test_status = False
        if self.isTestDefined(self.metric_identifier + "-1"):
            test_score = self.getTestConfigScore(self.metric_identifier + "-1")
            content_identifiers = self.fuji.content_identifier.values()
            if content_identifiers:
                if len(content_identifiers) > 0:
                    # here we only test the first content identifier
                    for data_link in content_identifiers:
                        data_url = data_link.get("url")
                        if data_url:
                            data_parsed_url = urlparse(data_url)
                            data_url_scheme = data_parsed_url.scheme
                            if data_url_scheme in self.fuji.STANDARD_PROTOCOLS:
                                self.logger.log(
                                    self.fuji.LOG_SUCCESS,
                                    self.metric_identifier
                                    + " : Standard protocol for access to data object found -: "
                                    + data_url_scheme,
                                )
                                self.data_output = {data_url_scheme: self.fuji.STANDARD_PROTOCOLS.get(data_url_scheme)}
                                self.setEvaluationCriteriumScore(self.metric_identifier + "-1", test_score, "pass")
                                self.maturity = self.getTestConfigMaturity(self.metric_identifier + "-1")
                                test_status = True
                                self.score.earned = test_score
                                break
            else:
                self.logger.warning(
                    self.metric_identifier
                    + " : Skipping protocol test for data since NO content (data) identifier is given in metadata"
                )
        return test_status

    def evaluate(self):
        self.result = StandardisedProtocolData(
            id=self.metric_number, metric_identifier=self.metric_identifier, metric_name=self.metric_name
        )

        test_status = "fail"
        if self.testStandardProtocolDataUsed():
            test_status = "pass"
        self.result.score = self.score
        self.result.output = StandardisedProtocolDataOutput(standard_data_protocol=self.data_output)
        self.result.metric_tests = self.metric_tests
        self.result.maturity = self.maturity
        self.result.test_status = test_status
