@echo off
set file=%1
cmd /k "act pull_request_target -e tests\data\%file%.json -W tests\data\workflow.yaml > log.log"
pause
exit