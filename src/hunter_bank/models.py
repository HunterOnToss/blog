# -*- coding: utf-8 -*-
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

SCORING_POINT = {1: "1", 2: "2"}


class Organization(models.Model):
    class Meta():
        db_table = "organization"

    EXVELLENT, GOOD, NORMALL, BAD, VERY_BAD = range(5)

    STATE = {EXVELLENT: u'Отлично',
             GOOD: u'Хорошо',
             NORMALL: u'Нормально',
             BAD: u'Плохо',
             VERY_BAD: u"Очень плохо"}

    organization_name = models.CharField(max_length=120)
    organization_status = models.SmallIntegerField(default=0, choices=STATE.items(), verbose_name=u'тип предложения')


class Offer(models.Model):
    class Meta():
        db_table = "offer"

    POTREB, IPOTEKA, AUTOCREDIT, KMCB = range(4)
    TYPE_STATE = {POTREB: u'потреб',
                  IPOTEKA: u'ипотека',
                  AUTOCREDIT: u'автокредит',
                  KMCB: u'КМСБ'}

    offer_create = models.DateTimeField()
    offer_update = models.DateTimeField()
    offer_rotation_begin = models.DateTimeField()
    offer_rotation_end = models.DateTimeField()
    offer_name = models.CharField(max_length=120)
    offer_type = models.SmallIntegerField(default=0, choices=TYPE_STATE.items(), verbose_name=u'тип предложения')
    offer_minimal_scoring_point = models.SmallIntegerField(default=0, choices=SCORING_POINT.items())
    offer_maximal_scoring_point = models.SmallIntegerField(default=0, choices=SCORING_POINT.items())
    offer_credit_organization = models.ForeignKey(Organization)


class Client(models.Model):
    class Meta():
        db_table = "client"

    client_create = models.DateTimeField()
    client_update = models.DateTimeField()
    client_name = models.CharField(max_length=48)
    client_family = models.CharField(max_length=48)
    client_otchestvo = models.CharField(max_length=48)
    client_birthday = models.DateTimeField()
    client_phone_number = PhoneNumberField()
    client_passport_number = models.IntegerField(max_length=20, verbose_name=u"Номер паспорта")
    client_scoring_point = models.SmallIntegerField(default=0, choices=SCORING_POINT.items())


class CreditApplication(models.Model):
    class Meta():
        db_table = "credit_application"

    NEW, SENT = range(2)
    STATUS = {
        NEW: u'Новый',
        SENT: u'Отправленный',
    }
    credit_application_create = models.DateTimeField()
    credit_application_send = models.DateTimeField()
    credit_application_client = models.ForeignKey(Client)
    credit_application_offer = models.ForeignKey(Offer)
    credit_application_status = models.SmallIntegerField(default=0, choices=STATUS.items(), verbose_name=u'Статус')