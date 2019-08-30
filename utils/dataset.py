from datasets.DAVIS import DAVIS, DAVISEval, DAVISInfer
from datasets.DAVIS3d import DAVIS3d
from datasets.DAVISProposalGuidance import DAVISProposalGuidance, DAVISProposalGuidanceEval, DAVISProposalGuidanceInfer
from datasets.YoutubeVOS import YoutubeVOSDataset
from utils.Constants import DAVIS_ROOT, YOUTUBEVOS_ROOT


def get_dataset(args):
  if args.train_dataset == "davis_proposal_guidance":
    trainset = DAVISProposalGuidance(DAVIS_ROOT, imset='2017/train.txt', is_train=True,
                     random_instance=args.random_instance, crop_size=args.crop_size, resize_mode=args.resize_mode,
                     max_temporal_gap=12, temporal_window=args.tw, augmentors=args.augmentors,
                     proposal_dir=args.proposal_dir)
  elif args.train_dataset == "davis":
    trainset = DAVIS(DAVIS_ROOT, imset='2017/train.txt', is_train=True,
                     random_instance=args.random_instance, crop_size=args.crop_size, resize_mode=args.resize_mode,
                     max_temporal_gap=12, temporal_window=args.tw, augmentors=args.augmentors,
                     proposal_dir=args.proposal_dir)
  elif args.train_dataset == "youtube_vos":
    trainset = YoutubeVOSDataset(YOUTUBEVOS_ROOT, imset='train', is_train=True,
                                 random_instance=args.random_instance, crop_size=args.crop_size,
                                 resize_mode=args.resize_mode, temporal_window=args.tw)
  elif args.train_dataset == "davis_3d":
    trainset = DAVIS3d(DAVIS_ROOT, imset='2017/train.txt', is_train=True,
                     random_instance=args.random_instance, crop_size=args.crop_size, resize_mode=args.resize_mode,
                     max_temporal_gap=12, temporal_window=args.tw, augmentors=args.augmentors,
                     proposal_dir=args.proposal_dir)

  if 'infer' in args.task:
    if 'davis_proposal_guidance' in args.test_dataset:
      testset = DAVISProposalGuidanceInfer(DAVIS_ROOT, random_instance=False, crop_size=args.crop_size_eval,
                           resize_mode=args.resize_mode_eval, temporal_window=args.tw, proposal_dir=args.proposal_dir)
    else:
       testset = DAVISInfer(DAVIS_ROOT, random_instance=False, crop_size=args.crop_size_eval,
                            resize_mode=args.resize_mode_eval, temporal_window=args.tw, proposal_dir=args.proposal_dir)
  elif 'davis_proposal_guidance' in args.test_dataset:
    testset = DAVISProposalGuidanceEval(DAVIS_ROOT, imset='2017/val.txt', random_instance=False, crop_size=args.crop_size_eval,
                        resize_mode=args.resize_mode_eval, temporal_window=args.tw, proposal_dir=args.proposal_dir)
  else:
    testset = DAVISEval(DAVIS_ROOT, imset='2017/val.txt', random_instance=False, crop_size=args.crop_size_eval,
                        resize_mode=args.resize_mode_eval, temporal_window=args.tw, proposal_dir=args.proposal_dir)

  return trainset, testset