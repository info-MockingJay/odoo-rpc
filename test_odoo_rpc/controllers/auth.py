from odoo import http
from odoo.http import request


class AuthController(http.Controller):
    @http.route('/api/info', type='json', auth='public', cors="*", csrf=False)
    def api_info(self, **kwargs):
        kwargs['message'] = "response info success."
        return kwargs

    @http.route('/api/login', type='json', auth='none', cors="*", csrf=False)
    def api_login(self, *args, **kwargs):
        db_name = http.request.db
        login = kwargs.get('login')
        password = kwargs.get('password')
        http.request.session.authenticate(db_name, login, password)
        return {"message": "login successfully."}

    @http.route('/api/signup', type='json', auth='public', cors="*", csrf=False, methods=['POST'])
    def api_signup(self, name, email, password, **kw):
        values = {
            "name": name,
            "login": email,
            "password": password
        }

        request.env["res.users"].sudo().signup(values)
        request.env.cr.commit()

        return {"message": "Signup Successfully"}
