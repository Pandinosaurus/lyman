import pytest
from moss import Bunch  # TODO change to lyman version when implemented


@pytest.fixture()
def lyman_info(tmpdir):
    data_dir = tmpdir.mkdir("data")
    analysis_dir = tmpdir.mkdir("analysis")
    cache_dir = tmpdir.mkdir("cache")

    # TODO probably get these from default info functions
    scan_info = {
        "subj01": {
            "sess01":
                {"exp_alpha": ["run01", "run02"]},
            "sess02":
                {"exp_alpha": ["run01"],
                 "exp_beta": ["run01", "run02", "run03"]},
        },
        "subj02": {
            "sess01":
                {"exp_alpha": ["run01", "run02", "run03"]}
        },
    }
    proj_info = Bunch(
        data_dir=str(data_dir),
        analysis_dir=str(analysis_dir),
        cache_dir=str(cache_dir),
        scan_info=scan_info,
        phase_encoding="pa",
        fm_template="{session}_fieldmap_{encoding}.nii.gz",
        ts_template="{session}_{experiment}_{run}.nii.gz",
        sb_template="{session}_{experiment}_{run}_sbref.nii.gz",
    )

    subjects = ["subj01", "subj02"]
    sessions = None

    exp_info = Bunch(name="exp_alpha")

    model_info = Bunch(name="model_info")

    return dict(
        proj_info=proj_info,
        subjects=subjects,
        sessions=sessions,
        exp_info=exp_info,
        model_info=model_info,
    )
