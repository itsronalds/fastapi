from fastapi import APIRouter, HTTPException, status
from fastapi.responses import HTMLResponse

router = APIRouter(prefix='/home', tags=['home'])


@router.get('/')
def render_home_page():
    try:
        with open('static/home.html', 'r', encoding='utf-8') as htmlfile:
            html_content = htmlfile.read()
        return HTMLResponse(html_content)
    except Exception as e:
        return HTTPException(status_code=status.HTTP_200_OK, detail={'message': 'Server internal error'})
