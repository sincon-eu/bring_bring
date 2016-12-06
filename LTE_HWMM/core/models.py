from datetime import date

from django.db import models


class TestData(models.Model):
    """
    Main class responsible of test name creation and storing its test results to postgres/mysql database
    """

    # TODO: choose life, choose future

    # i.e. uplink/downlink/cellular network class
    # transmission_class =

    # transmission_mode = models.
    # carrier_aggregation = models.CharField(default='')
    # direction = models.Bl
    # band_1 = models.ForeignKey()
    # band_2 = models.ForeignKey

    #
    test_type = models.ForeignKey('TestType')
    test_category = models.ForeignKey('TestCase')

    verdict_location = models.FilePathField(default='')
    ticket_url = models.URLField(default='', max_length=150)
    date_of_creation = models.DateTimeField(auto_now=True)
    date_of_last_modification = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{}_{}_{}'.format(self.carrier_aggregation_type,
                               self.band_1,
                               self.band_2,
                               )

    def generate_name(self):
        pass
    # TODO: sample test name
    # ICE_2CA_FDD_2A-12A_TM2564QAM_TM21064QAM


class TestType(models.Model):
    """
    Main test category. In the beginning it will be only for HWMM testing purposes.
    """
    pass


class TestCase(models.Model):
    """
    Basic test category i.e. Attach, Max UL T-put
    """
    pass


class HardwareType(models.Model):
    """
    Used for hardware declaration
    """
    pass


class SoftwareVersion(models.Model):
    """
    Used for driver version declaration
    """
    version_name = models.
    # AFAIK few release classes can exist
    version_class = models.CharField(max_length=10)

    def parse_name_to_date(self):
        return date =


class CarrierAggregationType(models.Model):
    """
    Specify number of component carriers
    """


class BandType(models.Model):
    # pass
    band_name = models.CharField(max_length=10)
    bandwidth = models.IntegerField(default=None)




class FunctionalTest(models.BooleanField):
    """
    Simple test data class
    """
    passed = models.BooleanField()
    date_of_test = models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'Passed = {}. Performed {}'.format(self.passed, self.date_of_test)


class PerformanceTest(FunctionalTest):
    """
    The same class as functional test
    """
    def __str__(self):
        return 'Passed = {}. Performed {}'.format(self.passed, self.date_of_test)


