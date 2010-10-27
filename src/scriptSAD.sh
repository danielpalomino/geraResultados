cd ../../jm-normal/
git checkout SAD_mode_decision
cd lencod/
make
cd ../../jm-heuristic/
git checkout SAD_mode_decision
cd lencod/
make
cd ../../GeraResultados/src/
python geraResultados.py

