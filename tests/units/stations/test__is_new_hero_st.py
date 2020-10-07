# coding: utf8
import pytest

from app.core.stations import IsNewHeroSt
from app.core.statuses import Statuses as Code


NEW_HERO = {
}

NOT_NEW_HERO = {
    "id": 123456789,
    "nick": "hero"
}

HERO_KEY = 'hero'


@pytest.mark.unit
@pytest.mark.core
@pytest.mark.stations
async def test__traveled_hero_is_new(train):
    train.states[HERO_KEY] = NEW_HERO
    status = await IsNewHeroSt(train).traveled()

    assert status == Code.IS_OK


@pytest.mark.unit
@pytest.mark.core
@pytest.mark.stations
async def test__traveled_hero_is_not_new(train):
    train.states[HERO_KEY] = NOT_NEW_HERO
    status = await IsNewHeroSt(train).traveled()

    assert status is Code.EMERGENCY_STOP


@pytest.mark.skip("Требуется `views.answers`.")
@pytest.mark.unit
@pytest.mark.core
@pytest.mark.stations
async def test__add_out_answer():
    """
    Добавить когда будет реализован пакет `app.views`.
    """
    pass