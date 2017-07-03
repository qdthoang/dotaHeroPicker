"""
Based on Amazon Alexa Skill Kit Example

Suggest a hero then close
"""

from __future__ import print_function
import random


# --------------- Helpers that build all of the responses ----------------------

def build_speechlet_response(title, output, reprompt_text, should_end_session):
    return {
        'outputSpeech': {
            'type': 'PlainText',
            'text': output
        },
        'card': {
            'type': 'Simple',
            'title': title,
            'content': output
        },
        'reprompt': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': reprompt_text
            }
        },
        'shouldEndSession': should_end_session
    }


def build_response(session_attributes, speechlet_response):
    return {
        'version': '1.0',
        'sessionAttributes': session_attributes,
        'response': speechlet_response
    }


# --------------- Functions that control the skill's behavior ------------------

def get_welcome_response():
    session_attributes = {}
    card_title = "Welcome"
    speech_output = "Welcome to Dota Hero Picker. " \
                    "Would you like a Dota hero suggestion?"
    reprompt_text = "Would you like a Dota hero suggestion?"
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))


def handle_session_end_request():
    card_title = "Session Ended"
    speech_output = "Thank you for trying the Dota Hero Picker. " \
                    "Have a nice day! "
    should_end_session = True
    return build_response({}, build_speechlet_response(
        card_title, speech_output, None, should_end_session))


hero_list = ['Abaddon',
             'Alchemist',
             'Ancient Apparition',
             'Anti-Mage',
             'Arc Warden',
             'Axe',
             'Bane',
             'Batrider',
             'Beastmaster',
             'Bloodseeker',
             'Bounty Hunter',
             'Brewmaster',
             'Bristleback',
             'Broodmother',
             'Centaur Warrunner',
             'Chaos Knight',
             'Chen',
             'Clinkz',
             'Clockwerk',
             'Crystal Maiden',
             'Dark Seer',
             'Dazzle',
             'Death Prophet',
             'Disruptor',
             'Doom',
             'Dragon Knight',
             'Drow Ranger',
             'Earth Spirit',
             'Earthshaker',
             'Elder Titan',
             'Ember Spirit',
             'Enchantress',
             'Enigma',
             'Faceless Void',
             'Gyrocopter',
             'Huskar',
             'Invoker',
             'Io',
             'Jakiro',
             'Juggernaut',
             'Keeper of the Light',
             'Kunkka',
             'Legion Commander',
             'Leshrac',
             'Lich',
             'Lifestealer',
             'Lina',
             'Lion',
             'Lone Druid',
             'Luna',
             'Lycan',
             'Magnus',
             'Medusa',
             'Meepo',
             'Mirana',
             'Monkey King',
             'Morphling',
             'Naga Siren',
             'Natures Prophet',
             'Necrophos',
             'Night Stalker',
             'Nyx Assassin',
             'Ogre Magi',
             'Omniknight',
             'Oracle',
             'Outworld Devourer',
             'Phantom Assassin',
             'Phantom Lancer',
             'Phoenix',
             'Puck',
             'Pudge',
             'Pugna',
             'Queen of Pain',
             'Razor',
             'Riki',
             'Rubick',
             'Sand King',
             'Shadow Demon',
             'Shadow Fiend',
             'Shadow Shaman',
             'Silencer',
             'Skywrath Mage',
             'Slardar',
             'Slark',
             'Sniper',
             'Spectre',
             'Spirit Breaker',
             'Storm Spirit',
             'Sven',
             'Techies',
             'Templar Assassin',
             'Terrorblade',
             'Tidehunter',
             'Timbersaw',
             'Tinker',
             'Tiny',
             'Treant Protector',
             'Troll Warlord',
             'Tusk',
             'Underlord',
             'Undying',
             'Ursa',
             'Vengeful Spirit',
             'Venomancer',
             'Viper',
             'Visage',
             'Warlock',
             'Weaver',
             'Windranger',
             'Winter Wyvern',
             'Witch Doctor',
             'Wraith King',
             'Zeus']

def randomize_hero():
    session_attributes = {}
    card_title = "Welcome"
    hero = random.choice(hero_list)
    speech_output = "You should play " + hero + ". Have fun!"
    reprompt_text = None
    should_end_session = True
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))



# --------------- Events ------------------

def on_session_started(session_started_request, session):
    """ Called when the session starts """

    print("on_session_started requestId=" + session_started_request['requestId']
          + ", sessionId=" + session['sessionId'])


def on_launch(launch_request, session):
    """ Called when the user launches the skill without specifying what they
    want
    """

    print("on_launch requestId=" + launch_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    # Dispatch to your skill's launch
    return get_welcome_response()


def on_intent(intent_request, session):
    """ Called when the user specifies an intent for this skill """

    print("on_intent requestId=" + intent_request['requestId'] +
          ", sessionId=" + session['sessionId'])

    intent = intent_request['intent']
    intent_name = intent_request['intent']['name']

    # Dispatch to your skill's intent handlers
    if intent_name == "RandomHeroPickerIntent":
        return randomize_hero()
    elif intent_name == "AMAZON.HelpIntent":
        return get_welcome_response()
    elif intent_name == "AMAZON.CancelIntent" or intent_name == "AMAZON.StopIntent":
        return handle_session_end_request()
    else:
        raise ValueError("Invalid intent")


def on_session_ended(session_ended_request, session):
    """ Called when the user ends the session.

    Is not called when the skill returns should_end_session=true
    """
    print("on_session_ended requestId=" + session_ended_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    # add cleanup logic here


# --------------- Main handler ------------------

def lambda_handler(event, context):
    """ Route the incoming request based on type (LaunchRequest, IntentRequest,
    etc.) The JSON body of the request is provided in the event parameter.
    """
    print("event.session.application.applicationId=" +
          event['session']['application']['applicationId'])

    """
    Uncomment this if statement and populate with your skill's application ID to
    prevent someone else from configuring a skill that sends requests to this
    function.
    """
    # if (event['session']['application']['applicationId'] !=
    #         "amzn1.echo-sdk-ams.app.[unique-value-here]"):
    #     raise ValueError("Invalid Application ID")

    if event['session']['new']:
        on_session_started({'requestId': event['request']['requestId']},
                           event['session'])

    if event['request']['type'] == "LaunchRequest":
        return on_launch(event['request'], event['session'])
    elif event['request']['type'] == "IntentRequest":
        return on_intent(event['request'], event['session'])
    elif event['request']['type'] == "SessionEndedRequest":
        return on_session_ended(event['request'], event['session'])
