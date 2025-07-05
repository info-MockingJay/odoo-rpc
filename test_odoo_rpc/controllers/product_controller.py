from odoo import http
from odoo.http import Controller, request


class ProductController(Controller):

    @http.route('/api/product', type='json', auth="public", website=True, sitemap=False, csrf=False, cors="*")
    def product_product(self, fields=False, offset=0, limit=False, domain=None, order=None, ):
        products = request.env["product.product"].sudo().web_search_read(domain, fields, offset=offset, limit=limit,
                                                                         order=order)

        return {'message': 'request successfully.', 'products': products}

    @http.route('/api/product/detail', type='json', auth="public", website=True, sitemap=False, csrf=False, cors="*")
    def product_detail(self, product_id, **kw):
        fields = kw.get("fields")
        product_detail = request.env["product.product"].sudo().search_read([["id", "=", product_id]], fields)
        return {"message": "Product Details", "product_detail": product_detail}


class ProductTemplateController(Controller):
    @http.route('/api/product/template', type='json', auth="public", website=True, sitemap=False, csrf=False, cors="*")
    def product_template(self, fields=False, offset=0, limit=False, domain=None, order=None, ):
        product_template = request.env["product.template"].sudo().web_search_read(domain, fields, offset=offset, limit=limit,
                                                                          order=order)

        return {'message': 'Product Template', 'product_template': product_template}

    @http.route('/api/product/template/detail', type='json', auth="public", website=True, sitemap=False, csrf=False, cors="*")
    def product_template_detail(self, product_template_id, **kw):
        fields = kw.get("fields")
        product_template_detail = request.env["product.template"].sudo().search_read([["id", "=", product_template_id]], fields)
        return {"message": "Product Template Details", "product_template_detail": product_template_detail}


class ProductCategoryController(Controller):
    @http.route('/api/product/category', type='json', auth="public", website=True, sitemap=False, csrf=False, cors="*")
    def product_category(self, fields=False, offset=0, limit=False, domain=None, order=None, ):
        product_category = request.env["product.public.category"].sudo().web_search_read(domain, fields, offset=offset,
                                                                                 limit=limit, order=order)

        return {'message': 'Product Category', 'product_category': product_category}

    @http.route('/api/product/category/detail', type='json', auth="public", website=True, sitemap=False, csrf=False, cors="*")
    def product_category_detail(self, category_id, **kw):
        fields = kw.get("fields")
        product_category_detail = request.env["product.public.category"].sudo().search_read([["id", "=", category_id]], fields)
        return {"message": "Product Category Details", "product_category_detail": product_category_detail}
