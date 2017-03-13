#! /usr/bin/env python

import argparse
from pkg_resources import resource_filename, Requirement
from bauto.predict import predict_brain_age_single_subject

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='BAuto: automatic prediction of Brain Age. Files mode. '
                                                 'You specify lh/rh thickness/area + aseg file (with '
                                                 '--lh_thickness_file...). Surface files need to be sampled to '
                                                 'fsaverage4 space, aseg files extracted via asegstats2table. Only '
                                                 'one subject can be specified at a time.')
    parser.add_argument('out_dir', help='Results are put here.')
    parser.add_argument('--participant_label', help='will be written into output files and can be omitted')
    parser.add_argument('--model', choices=["Liem2016__OCI_norm"], default="Liem2016__OCI_norm", help='')

    parser.add_argument('--lh_thickness_file', required=True, help='')
    parser.add_argument('--rh_thickness_file', required=True, help='')
    parser.add_argument('--lh_area_file', required=True, help='')
    parser.add_argument('--rh_area_file', required=True, help='')
    parser.add_argument('--aseg_file', required=True, help='')

    args = parser.parse_args()

    model_dir = resource_filename(Requirement.parse("bauto"), 'models')

    if args.participant_label:
        subject = args.participant_label
    else:
        subject = ""
    predict_brain_age_single_subject(out_dir=args.out_dir,
                                     lh_thickness_file=args.lh_thickness_file,
                                     rh_thickness_file=args.rh_thickness_file,
                                     lh_area_file=args.lh_area_file,
                                     rh_area_file=args.rh_area_file,
                                     aseg_file=args.aseg_file,
                                     model_dir=model_dir,
                                     model=args.model,
                                     subject_label=subject)
