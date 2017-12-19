import pytest
import day_20171218 as e


def test_get_val():
    value_string = 'a'
    status = {
        'last_played': None,
        'recovered': None,
        'registers': {'a': 1}} 
    assert e.get_val(value_string, status) == 1
    value_string = 2
    status = {
        'last_played': None,
        'recovered': None,
        'registers': {'a': 1}} 
    assert e.get_val(value_string, status) == 2


def test_apply_snd():
    instruction = ['snd', 'a']
    status = {
        'last_played': None,
        'recovered': None,
        'registers': {'a': 1}} 
    new_status = {
        'last_played': 1,
        'recovered': None,
        'registers': {'a': 1}} 
    assert e.apply_snd(instruction, status) == new_status


def test_apply_set():
    instruction = ['set', 'a', '2']
    status = {
        'last_played': None,
        'recovered': None,
        'registers': {'a': 0}} 
    new_status = {
        'last_played': None,
        'recovered': None,
        'registers': {'a': 2}} 
    assert e.apply_set(instruction, status) == new_status


def test_apply_add():
    instruction = ['add', 'a', '2']
    status = {
        'last_played': None,
        'recovered': None,
        'registers': {'a': 0}} 
    new_status = {
        'last_played': None,
        'recovered': None,
        'registers': {'a': 2}} 
    assert e.apply_add(instruction, status) == new_status

    instruction = ['add', 'a', 'a']
    status = {
        'last_played': None,
        'recovered': None,
        'registers': {'a': 2}} 
    new_status = {
        'last_played': None,
        'recovered': None,
        'registers': {'a': 4}} 
    assert e.apply_add(instruction, status) == new_status


def test_apply_mul():
    instruction = ['mul', 'a', '2']
    status = {
        'last_played': None,
        'recovered': None,
        'registers': {'a': 3}} 
    new_status = {
        'last_played': None,
        'recovered': None,
        'registers': {'a': 6}} 
    assert e.apply_mul(instruction, status) == new_status

    instruction = ['mul', 'a', 'b']
    status = {
        'last_played': None,
        'recovered': None,
        'registers': {'a': 3, 'b': 2}} 
    new_status = {
        'last_played': None,
        'recovered': None,
        'registers': {'a': 6, 'b': 2}} 
    assert e.apply_mul(instruction, status) == new_status

def test_apply_mod():
    instruction = ['mod', 'a', '2']
    status = {
        'last_played': None,
        'recovered': None,
        'registers': {'a': 3}} 
    new_status = {
        'last_played': None,
        'recovered': None,
        'registers': {'a': 1}} 
    assert e.apply_mod(instruction, status) == new_status

    instruction = ['mod', 'a', 'b']
    status = {
        'last_played': None,
        'recovered': None,
        'registers': {'a': 5, 'b': 3}} 
    new_status = {
        'last_played': None,
        'recovered': None,
        'registers': {'a': 2, 'b': 3}} 
    assert e.apply_mod(instruction, status) == new_status

def test_apply_rcv():
    instruction = ['rcv', 'a']
    status = {
        'last_played': 5,
        'recovered': None,
        'registers': {'a': 0}} 
    new_status = {
        'last_played': 5,
        'recovered': None,
        'registers': {'a': 0}} 
    assert e.apply_rcv(instruction, status) == new_status

    instruction = ['rcv', 'a']
    status = {
        'last_played': 5,
        'recovered': None,
        'registers': {'a': 1}} 
    new_status = {
        'last_played': 5,
        'recovered': 5,
        'registers': {'a': 1}} 
    assert e.apply_rcv(instruction, status) == new_status


def test_apply_jgz():
    instruction = ['jgz', 'a', '-3']
    status = {
        'last_played': 5,
        'recovered': None,
        'registers': {'a': 0}} 
    jump = 1
    assert e.apply_jgz(instruction, status) == jump

    instruction = ['jgz', 'a', '-3']
    status = {
        'last_played': 5,
        'recovered': None,
        'registers': {'a': 4}} 
    jump = -3
    assert e.apply_jgz(instruction, status) == jump
