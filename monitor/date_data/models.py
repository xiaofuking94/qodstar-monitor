from django.db import models
from django.utils.translation import ugettext_lazy as _


class DateData(models.Model):
    """
    record date_data every through cronjob
  
    fields include:
      -- pc_page_view
      -- wx_page_view
      -- increased_user_amount
      -- jobpost_amount
      -- invitation_sent_amount
      -- sale_amount
      -- potential_user_amount
    """
    created = models.DateField(auto_now_add=True)
    
    pc_page_view = models.PositiveIntegerField(
      help_text=_('网页端每天浏览量'),
      default=0,
      null=False,
      blank=True
    )
    
    wx_page_view = models.PositiveIntegerField(
      help_text=_('公众号每天浏览量'),
      default=0,
      null=False,
      blank=True
    )
    
    increased_user_amount = models.PositiveIntegerField(
      help_text=_('每天新增的企业用户'),
      default=0,
      null=False,
      blank=True
    )
    
    jobpost_amount = models.PositiveIntegerField(
      help_text=_('每天新增职位'),
      default=0,
      null=False,
      blank=True
    )
    
    invitation_sent_amount = models.PositiveIntegerField(
      help_text=_('每天邀请发送的数量'),
      default=0,
      null=False,
      blank=True
    )
    
    sale_amount = models.PositiveIntegerField(
      help_text=_('每天的销售额'),
      default=0,
      null=False,
      blank=True
    )

    potential_user_amount = models.PositiveIntegerField(
      help_text=_('潜在用户（报名公测用户）'),
      default=0,
      null=False,
      blank=True
    )
    
    new_user_amount = models.PositiveIntegerField(
      help_text=_('新用户，已注册的用户'),
      default=0,
      null=False,
      blank=True
    )
    
    real_user_amount = models.PositiveIntegerField(
      help_text=_('真实用户数量，即已发送测试邀请的企业用户'),
      default=0,
      null=False,
      blank=True
    )
    
    class Meta:
        
        # indexes = [
        #   models.Index(fields=['id', ''])
        # ]
        ordering = ('-created', )
