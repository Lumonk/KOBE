#
# This is to convert .str files into .id files with dict files
#
import argparse
import utils

parser = argparse.ArgumentParser(description='preprocess.py')
parser.add_argument('--src_str', default='./dataloading/src.str', type=str,
                    help='string type source file location')
parser.add_argument('--tgt_str', default='./dataloading/tgt.str', type=str,
                    help='string type target file location')
parser.add_argument('--src_dict', default='./dataloading/src.dict', type=str, 
                    help='location of dictionary of the source file')
parser.add_argument('--tgt_dict', default='./dataloading/tgt.dict', type=str, 
                    help='location of dictionary of the target file')
parser.add_argument('--save', default='./dataloading/', type=str, 
                    help='save location')
parser.add_argument('--src_char', action='store_true',
                    help='character based encoding')
parser.add_argument('-tgt_char', action='store_true',
                    help='character based decoding')
parser.add_argument('--lower', action='store_true',
                    help='lower the case')
parser.add_argument('--report_every', type=int, default=1,
                    help="Report status every this many sentences")
opt = parser.parse_args()


def makeData(srcFile, tgtFile, srcDicts, tgtDicts, save):
    sizes = 0
    count, empty_ignored = 0, 0

    print('Processing %s & %s ...' % (srcFile, tgtFile))
    srcF = open(srcFile, encoding='utf8')
    tgtF = open(tgtFile, encoding='utf8')

    srcIdF = open(opt.save + 'src.id', 'w')
    tgtIdF = open(opt.save + 'tgt.id', 'w')


    while True:
        sline = srcF.readline()
        tline = tgtF.readline()

        # normal end of file
        if sline == "" and tline == "":
            break

        # source or target does not have same number of lines
        if sline == "" or tline == "":
            print('WARNING: source and target do not have the same number of sentences')
            break

        sline = sline.strip()
        tline = tline.strip()

        # source and/or target are empty
        if sline == "" or tline == "":
            print('WARNING: ignoring an empty line ('+str(count+1)+')')
            empty_ignored += 1
            continue

        if opt.lower:
            sline = sline.lower()
            tline = tline.lower()

        srcWords = sline.split() if not opt.src_char else list(sline)
        tgtWords = tline.split() if not opt.tgt_char else list(tline)

		# add filter here later!

        srcIds = srcDicts.convertToIdx(srcWords, utils.UNK_WORD)
        tgtIds = tgtDicts.convertToIdx(tgtWords, utils.UNK_WORD, utils.BOS_WORD, utils.EOS_WORD)

        srcIdF.write(" ".join(list(map(str, srcIds)))+'\n')
        tgtIdF.write(" ".join(list(map(str, tgtIds)))+'\n')

        sizes += 1
        if sizes % opt.report_every == 0:
            print('... %d sentences prepared' % sizes)

    srcF.close()
    tgtF.close()
    srcIdF.close()
    tgtIdF.close()


    return {'srcIdF': save + '.id', 'tgtIdF': save + '.id',
           }


def main():
    dicts={}
    dicts['src'] = utils.Dict(data=opt.src_dict, lower=opt.lower)
    dicts['tgt'] = utils.Dict(data=opt.tgt_dict, lower=opt.lower)
    data = makeData(opt.src_str, opt.tgt_str, dicts['src'], dicts['tgt'] ,opt.save)
    
    


if __name__ == "__main__":
    main()
