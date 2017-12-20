import pytest
import day_20171218 as e



def test_apply_snd():
    instruction = ['snd', 'a']
    status1 = {
        'program': 1,
        'terminated': False,
        'sent_counter': 0,
        'queue': [],
        'registers': {'a': 1}} 
    status2 = {
        'program': 2,
        'terminated': False,
        'sent_counter': 0,
        'queue': [],
        'registers': {}} 
    new_status1 = {
        'program': 1,
        'terminated': False,
        'sent_counter': 1,
        'queue': [],
        'registers': {'a': 1}} 
    new_status2 = {
        'program': 2,
        'terminated': False,
        'sent_counter': 0,
        'queue': [1],
        'registers': {}} 
    assert e.apply_snd(instruction, status1, status2) == (new_status1, new_status2)


def test_apply_rcv():
    instruction = ['rcv', 'a']
    status = {
        'program': 1,
        'terminated': False,
        'sent_counter': 0,
        'queue': [1, 2],
        'registers': {'a': 0}} 
    new_status = {
        'program': 1,
        'terminated': False,
        'sent_counter': 0,
        'queue': [2],
        'registers': {'a': 1}} 
    assert e.apply_rcv(instruction, status) == new_status

    instruction = ['rcv', 'a']
    status = {
        'program': 1,
        'terminated': False,
        'sent_counter': 0,
        'queue': [],
        'registers': {'a': 0}} 
    new_status = {
        'program': 1,
        'terminated': True,
        'sent_counter': 0,
        'queue': [],
        'registers': {'a': 0}} 
    assert e.apply_rcv(instruction, status) == new_status
