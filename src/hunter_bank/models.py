# -*- coding: utf-8 -*-
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

SCORING_POINT = {1: "10%", 2: "20%", 3: "30%", 4: "40%", 5: "50%",
                 6: "60%", 7: "70%", 8: "80%", 9: "90%", 10: "100%"}


class Organization(models.Model):
    class Meta():
        db_table = "organization"
        verbose_name_plural = u"Парнер"

    EXVELLENT, GOOD, NORMALL, BAD, VERY_BAD = range(5)

    STATE = {EXVELLENT: u'Отлично',
             GOOD: u'Хорошо',
             NORMALL: u'Нормально',
             BAD: u'Плохо',
             VERY_BAD: u"Очень плохо"}

    organization_name = models.CharField(max_length=120, verbose_name=u"Партнер")
    organization_status = models.SmallIntegerField(default=0, choices=STATE.items(), verbose_name=u'Тип предложения')

    def __unicode__(self):
        return self.organization_name


class Offer(models.Model):
    class Meta():
        db_table = "offer"
        verbose_name = u"Предложение"
        verbose_name_plural = u"Предложения"

    POTREB, IPOTEKA, AUTOCREDIT, KMCB = range(4)
    TYPE_STATE = {POTREB: u'потреб',
                  IPOTEKA: u'ипотека',
                  AUTOCREDIT: u'автокредит',
                  KMCB: u'КМСБ'}

    offer_create = models.DateTimeField(auto_now_add=True, verbose_name=u"Дата создания")
    offer_update = models.DateTimeField(auto_now=True, verbose_name=u"Дата изменения")
    offer_rotation_begin = models.DateTimeField(verbose_name=u"Начало ротации")
    offer_rotation_end = models.DateTimeField(verbose_name=u"Окончание ротации")
    offer_name = models.CharField(max_length=120, verbose_name=u"Название предложения")
    offer_type = models.SmallIntegerField(default=0, choices=TYPE_STATE.items(), verbose_name=u'Тип предложения')
    offer_minimal_scoring_point = models.SmallIntegerField(default=0, choices=SCORING_POINT.items(),
                                                           verbose_name=u"Минимальный скоринговый балл")
    offer_maximal_scoring_point = models.SmallIntegerField(default=0, choices=SCORING_POINT.items(),
                                                           verbose_name=u"Максимальный скоринговый балл")
    offer_credit_organization = models.ForeignKey(Organization, verbose_name=u"Кредитная оргонизация")

    def __unicode__(self):
        return self.offer_name


class Client(models.Model):
    class Meta():
        db_table = "client"
        verbose_name = u"Анкета клиента"
        verbose_name_plural = u"Анкеты клиентов"

    ID = models.AutoField(primary_key=True)
    client_create = models.DateTimeField(auto_now_add=True, verbose_name=u"Дата создания")
    client_update = models.DateTimeField(auto_now=True, verbose_name=u"Дата изменения")
    client_name = models.CharField(max_length=48, verbose_name=u"Имя клиента")
    client_family = models.CharField(max_length=48, verbose_name=u"Фамилия клиента")
    client_otchestvo = models.CharField(max_length=48, verbose_name=u"Отчество клиента")
    client_birthday = models.DateField(verbose_name=u"Дата рождения клиента")
    client_phone_number = PhoneNumberField(verbose_name=u"Номер телефона")
    client_passport_number = models.IntegerField(max_length=20, verbose_name=u"Номер паспорта")
    client_scoring_point = models.SmallIntegerField(default=0, choices=SCORING_POINT.items(),
                                                    verbose_name=u"скоринговый балл")

    def __unicode__(self):
        return self.client_family


class CreditApplication(models.Model):
    class Meta():
        db_table = "credit_application"

    NEW, SENT = range(2)
    STATUS = {
        NEW: u'Новый',
        SENT: u'Отправленный',
    }
    credit_application_create = models.DateTimeField(auto_now_add=True, verbose_name=u"Дата создания")
    credit_application_send = models.DateTimeField(blank=True, null=True, verbose_name=u"Дата отправки")
    credit_application_client = models.ForeignKey(Client)
    credit_application_offer = models.ForeignKey(Offer)
    credit_application_status = models.SmallIntegerField(default=0, choices=STATUS.items(), verbose_name=u'Статус')