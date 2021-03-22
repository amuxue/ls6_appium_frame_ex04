from frame.app import App


def test_search():
    app=App()
    # app.start()
    result=app.start().goto_main().goto_market_page().goto_search().search()
    assert result