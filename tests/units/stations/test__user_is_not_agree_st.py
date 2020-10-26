# coding: utf8
import pytest

from app.core.stations import UserIsNotAgreeSt
from app.database.fixture import Languages
from app.core.statuses import Statuses as Code
from app.database.queries import User
from tests.helpers.fake_executions import fake_execution_with_error
from tests.helpers.fake_executions import fake_execution_empty


@pytest.fixture()
def up_train(train):
    train.states["user"] = {"language": Languages.RUSSIAN}
    return train


@pytest.mark.unit
@pytest.mark.core
@pytest.mark.stations
async def test__traveled(up_train, monkeypatch):
    train = up_train
    monkeypatch.setattr(UserIsNotAgreeSt, "execution", fake_execution_empty)
    status = await UserIsNotAgreeSt(train).traveled()
    assert status is Code.IS_OK


@pytest.mark.unit
@pytest.mark.core
@pytest.mark.stations
async def test__traveled_with_error(up_train, monkeypatch):
    train = up_train
    monkeypatch.setattr(
        UserIsNotAgreeSt, "execution", fake_execution_with_error)
    status = await UserIsNotAgreeSt(train).traveled()

    assert status is Code.EMERGENCY_STOP


@pytest.mark.unit
@pytest.mark.core
@pytest.mark.stations
async def test__query_data(up_train):
    train = up_train
    query_name = UserIsNotAgreeSt(train).query_data()
    query_data = train.queries[query_name]
    assert query_data.get("id")


@pytest.mark.unit
@pytest.mark.core
@pytest.mark.stations
async def test__storage_query(train):
    storage_query = UserIsNotAgreeSt(train).storage_query()
    bound_method = User.is_not_agree_policy
    assert storage_query == bound_method


@pytest.mark.skip("Требуется `views.answers`.")
@pytest.mark.unit
@pytest.mark.core
@pytest.mark.stations
async def test__add_out_answer():
    """
    Добавить когда будет реализован пакет `app.views`.
    """
    pass
