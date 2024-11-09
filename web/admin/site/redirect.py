# coding:utf-8

# ---------------------------------------------------------------------------------
# MW-Linux面板
# ---------------------------------------------------------------------------------
# copyright (c) 2018-∞(https://github.com/midoks/mdserver-web) All rights reserved.
# ---------------------------------------------------------------------------------
# Author: midoks <midoks@163.com>
# ---------------------------------------------------------------------------------

import os
import json

from flask import Blueprint, render_template
from flask import request

from admin.user_login_check import panel_login_required

from utils.plugin import plugin as MwPlugin
from utils.site import sites as MwSites
import utils.site as site
import core.mw as mw
import thisdb

from .site import blueprint

# 获取重定向列表
@blueprint.route('/get_redirect', endpoint='get_redirect', methods=['POST'])
@panel_login_required
def get_redirect():
    site_name = request.form.get("siteName", '')
    return MwSites.instance().getRedirect(site_name)

# 设置重定向列表
@blueprint.route('/set_redirect', endpoint='set_redirect', methods=['POST'])
@panel_login_required
def set_redirect():
    site_name = request.form.get("siteName", '')
    site_from = request.form.get("from", '')
    to = request.form.get("to", '')                 # redirect to
    type = request.form.get("type", '')             # path / domain
    r_type = request.form.get("r_type", '')         # redirect type
    keep_path = request.form.get("keep_path", '')   # keep path
    return MwSites.instance().setRedirect(site_name, site_from, to, type, r_type, keep_path)

# 设置重定向配置
@blueprint.route('/get_redirect_conf', endpoint='get_redirect_conf', methods=['POST'])
@panel_login_required
def get_redirect_conf():
    site_name = request.form.get("siteName", '')
    rid = request.form.get("id", '')
    return MwSites.instance().getRedirectConf(site_name, rid) 






