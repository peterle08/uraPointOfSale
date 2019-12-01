from behave import *
from flask import url_for
from time import sleep

@given('I am on the landing page')
def step_impl(context):
    with context.context:
        context.browser.visit(url_for('app.index'))
        assert(context.browser.url == url_for('app.index'))

@given('I am on the about page')
def step_impl(context):
    with context.request:
        context.browser.visit(url_for('about'))
        assert(context.browser.url == url_for('about'))

@then('I see the company name')
def step_impl(context):
    assert(context.browser.is_text_present("Note Weaver"))

@then('I see a link to "{link}"')
def step_impl(context, link):
    assert(context.browser.find_link_by_href(link))

@then('I see the navigation bar')
def step_impl(context):
    assert(context.browser.find_by_css('.navbar'))

@then('I can navigate to other pages')
def step_impl(context):
    with context.context:
        context.browser.find_link_by_href('/about').first.click()
        sleep(0.5)
        assert(context.browser.url == url_for('app.about'))

@given('I am registered')
def step_impl(context):
    with context.context:
        context.browser.visit(url_for('app.register'))
        context.browser.find_by_xpath("//input[@name='email']").fill('exampleuser@exampleuser.com')
        context.browser.find_by_xpath("//input[@name='username']").fill('exampleusername')
        context.browser.find_by_xpath("//input[@name='password']").fill('ExamplePa33word!')
        context.browser.find_by_xpath("//input[@name='password_confirm']").fill('ExamplePa33word!')
        context.browser.find_by_xpath("//input[@name='submit']").first.click()
        sleep(0.5)
        assert(context.browser.url == url_for('app.login'))

@given('I am logged in')
def step_impl(context):
    assert(False)

@given('I am not logged in')
def step_impl(context):
    assert(False)

@then('I see the text "{text}"')
def step_impl(context, text):
    with context.context:
        assert(context.browser.is_text_present(text))

@then('I see the image company logo')
def step_impl(context):
    with context.request:
        assert(not context.browser.is_element_not_present_by_id('company logo'))

