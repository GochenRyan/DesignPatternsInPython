import prototype
import copy

if __name__ == '__main__':
    oResume = prototype.CResume("aa")
    oResume.SetWorkExperience("20190701", "RNG")

    oResume0 = copy.deepcopy(oResume)
    oResume0.SetWorkExperience("20200402", "iG")

    print oResume
    print oResume0

    oResume1 = copy.copy(oResume)
    oResume1.SetWorkExperience("20200402", "EDG")

    print oResume
    print oResume1
