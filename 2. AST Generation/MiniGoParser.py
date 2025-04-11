# Generated from main/MiniGo.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3E")
        buf.write("\u024c\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\3\2\5")
        buf.write("\2v\n\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\5\3\u0082")
        buf.write("\n\3\3\4\3\4\3\4\3\5\3\5\3\5\3\5\5\5\u008b\n\5\3\6\3\6")
        buf.write("\3\6\5\6\u0090\n\6\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\t\3\t")
        buf.write("\3\t\3\t\3\t\5\t\u009e\n\t\3\n\3\n\3\n\3\n\3\n\5\n\u00a5")
        buf.write("\n\n\3\13\3\13\3\13\3\f\3\f\3\f\3\f\5\f\u00ae\n\f\3\f")
        buf.write("\3\f\5\f\u00b2\n\f\3\f\3\f\3\f\5\f\u00b7\n\f\3\f\5\f\u00ba")
        buf.write("\n\f\3\r\3\r\3\r\3\r\3\r\3\r\5\r\u00c2\n\r\3\16\3\16\3")
        buf.write("\16\3\16\5\16\u00c8\n\16\3\17\3\17\3\20\3\20\3\20\5\20")
        buf.write("\u00cf\n\20\3\20\3\20\3\21\3\21\3\21\3\22\3\22\3\22\3")
        buf.write("\22\3\22\3\22\3\22\5\22\u00dd\n\22\3\23\3\23\3\23\5\23")
        buf.write("\u00e2\n\23\3\23\3\23\3\24\3\24\3\24\3\24\5\24\u00ea\n")
        buf.write("\24\3\24\3\24\5\24\u00ee\n\24\3\24\3\24\3\24\3\25\3\25")
        buf.write("\3\25\3\25\3\25\5\25\u00f8\n\25\3\25\3\25\5\25\u00fc\n")
        buf.write("\25\3\26\3\26\3\26\3\26\5\26\u0102\n\26\3\26\3\26\5\26")
        buf.write("\u0106\n\26\3\26\3\26\3\26\3\27\3\27\3\27\5\27\u010e\n")
        buf.write("\27\3\27\3\27\5\27\u0112\n\27\3\27\3\27\5\27\u0116\n\27")
        buf.write("\3\30\3\30\3\30\3\30\5\30\u011c\n\30\3\30\3\30\5\30\u0120")
        buf.write("\n\30\3\30\5\30\u0123\n\30\3\30\3\30\3\31\3\31\3\31\3")
        buf.write("\31\5\31\u012b\n\31\3\32\3\32\5\32\u012f\n\32\3\32\3\32")
        buf.write("\5\32\u0133\n\32\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3")
        buf.write("\33\5\33\u013d\n\33\3\33\3\33\5\33\u0141\n\33\3\33\5\33")
        buf.write("\u0144\n\33\3\33\3\33\3\34\3\34\3\34\3\34\5\34\u014c\n")
        buf.write("\34\3\35\3\35\3\35\5\35\u0151\n\35\3\36\3\36\3\37\3\37")
        buf.write("\3\37\3\37\5\37\u0159\n\37\3 \3 \3 \3 \3 \3 \3 \3 \5 ")
        buf.write("\u0163\n \3 \3 \3!\3!\3!\3!\3\"\3\"\5\"\u016d\n\"\3#\3")
        buf.write("#\5#\u0171\n#\3#\5#\u0174\n#\3#\3#\3$\3$\3$\3$\3$\5$\u017d")
        buf.write("\n$\3$\3$\3$\3$\5$\u0183\n$\3$\5$\u0186\n$\3%\3%\3%\3")
        buf.write("%\3%\3%\5%\u018e\n%\3%\3%\3%\3%\5%\u0194\n%\3&\3&\5&\u0198")
        buf.write("\n&\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\5\'\u01a2\n\'\3\'")
        buf.write("\3\'\3(\3(\3(\3(\3(\3(\5(\u01ac\n(\3(\3(\5(\u01b0\n(\3")
        buf.write("(\3(\3(\3(\3(\3(\3(\5(\u01b9\n(\3(\3(\3)\3)\3*\3*\3+\3")
        buf.write("+\3+\5+\u01c4\n+\3+\3+\3,\3,\3,\3,\3,\5,\u01cd\n,\3-\3")
        buf.write("-\3-\3-\3-\3-\7-\u01d5\n-\f-\16-\u01d8\13-\3.\3.\3.\3")
        buf.write(".\3.\3.\7.\u01e0\n.\f.\16.\u01e3\13.\3/\3/\3/\3/\3/\3")
        buf.write("/\7/\u01eb\n/\f/\16/\u01ee\13/\3\60\3\60\3\60\3\60\3\60")
        buf.write("\3\60\7\60\u01f6\n\60\f\60\16\60\u01f9\13\60\3\61\3\61")
        buf.write("\3\61\3\61\3\61\3\61\7\61\u0201\n\61\f\61\16\61\u0204")
        buf.write("\13\61\3\62\3\62\3\62\5\62\u0209\n\62\3\63\3\63\3\63\3")
        buf.write("\63\3\63\3\63\5\63\u0211\n\63\3\63\3\63\3\63\3\63\3\63")
        buf.write("\3\63\3\63\3\63\3\63\7\63\u021c\n\63\f\63\16\63\u021f")
        buf.write("\13\63\3\64\3\64\3\64\3\64\3\64\3\64\3\64\5\64\u0228\n")
        buf.write("\64\3\65\3\65\3\65\5\65\u022d\n\65\3\65\3\65\3\66\3\66")
        buf.write("\5\66\u0233\n\66\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3")
        buf.write("\67\7\67\u023d\n\67\f\67\16\67\u0240\13\67\38\38\39\3")
        buf.write("9\59\u0246\n9\3:\3:\5:\u024a\n:\3:\2\tXZ\\^`dl;\2\4\6")
        buf.write("\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\66")
        buf.write("8:<>@BDFHJLNPRTVXZ\\^`bdfhjlnpr\2\f\5\2\24\26\67;>>\3")
        buf.write("\2\17\20\4\2\67\679;\3\2\13\16\3\2\34!\3\2\27\30\3\2\31")
        buf.write("\33\4\2\30\30++\3\2%*\4\2\65\65AA\2\u026a\2u\3\2\2\2\4")
        buf.write("\u0081\3\2\2\2\6\u0083\3\2\2\2\b\u008a\3\2\2\2\n\u008f")
        buf.write("\3\2\2\2\f\u0091\3\2\2\2\16\u0093\3\2\2\2\20\u009d\3\2")
        buf.write("\2\2\22\u00a4\3\2\2\2\24\u00a6\3\2\2\2\26\u00b9\3\2\2")
        buf.write("\2\30\u00bb\3\2\2\2\32\u00c3\3\2\2\2\34\u00c9\3\2\2\2")
        buf.write("\36\u00cb\3\2\2\2 \u00d2\3\2\2\2\"\u00d5\3\2\2\2$\u00de")
        buf.write("\3\2\2\2&\u00e5\3\2\2\2(\u00f7\3\2\2\2*\u00fd\3\2\2\2")
        buf.write(",\u010a\3\2\2\2.\u0117\3\2\2\2\60\u0126\3\2\2\2\62\u012c")
        buf.write("\3\2\2\2\64\u0134\3\2\2\2\66\u014b\3\2\2\28\u0150\3\2")
        buf.write("\2\2:\u0152\3\2\2\2<\u0158\3\2\2\2>\u0162\3\2\2\2@\u0166")
        buf.write("\3\2\2\2B\u016a\3\2\2\2D\u016e\3\2\2\2F\u0177\3\2\2\2")
        buf.write("H\u0193\3\2\2\2J\u0197\3\2\2\2L\u0199\3\2\2\2N\u01a5\3")
        buf.write("\2\2\2P\u01bc\3\2\2\2R\u01be\3\2\2\2T\u01c0\3\2\2\2V\u01cc")
        buf.write("\3\2\2\2X\u01ce\3\2\2\2Z\u01d9\3\2\2\2\\\u01e4\3\2\2\2")
        buf.write("^\u01ef\3\2\2\2`\u01fa\3\2\2\2b\u0208\3\2\2\2d\u020a\3")
        buf.write("\2\2\2f\u0227\3\2\2\2h\u0229\3\2\2\2j\u0232\3\2\2\2l\u0234")
        buf.write("\3\2\2\2n\u0241\3\2\2\2p\u0243\3\2\2\2r\u0247\3\2\2\2")
        buf.write("tv\5p9\2ut\3\2\2\2uv\3\2\2\2vw\3\2\2\2wx\5\b\5\2xy\7\2")
        buf.write("\2\3y\3\3\2\2\2z\u0082\5\"\22\2{\u0082\5$\23\2|\u0082")
        buf.write("\5&\24\2}\u0082\5\30\r\2~\u0082\5.\30\2\177\u0082\5*\26")
        buf.write("\2\u0080\u0082\5\64\33\2\u0081z\3\2\2\2\u0081{\3\2\2\2")
        buf.write("\u0081|\3\2\2\2\u0081}\3\2\2\2\u0081~\3\2\2\2\u0081\177")
        buf.write("\3\2\2\2\u0081\u0080\3\2\2\2\u0082\5\3\2\2\2\u0083\u0084")
        buf.write("\5\4\3\2\u0084\u0085\5p9\2\u0085\7\3\2\2\2\u0086\u0087")
        buf.write("\5\6\4\2\u0087\u0088\5\b\5\2\u0088\u008b\3\2\2\2\u0089")
        buf.write("\u008b\5\6\4\2\u008a\u0086\3\2\2\2\u008a\u0089\3\2\2\2")
        buf.write("\u008b\t\3\2\2\2\u008c\u0090\5\f\7\2\u008d\u0090\5\16")
        buf.write("\b\2\u008e\u0090\5\26\f\2\u008f\u008c\3\2\2\2\u008f\u008d")
        buf.write("\3\2\2\2\u008f\u008e\3\2\2\2\u0090\13\3\2\2\2\u0091\u0092")
        buf.write("\t\2\2\2\u0092\r\3\2\2\2\u0093\u0094\5\24\13\2\u0094\u0095")
        buf.write("\7\63\2\2\u0095\u0096\5\20\t\2\u0096\u0097\7\64\2\2\u0097")
        buf.write("\17\3\2\2\2\u0098\u0099\5\22\n\2\u0099\u009a\7\62\2\2")
        buf.write("\u009a\u009b\5\20\t\2\u009b\u009e\3\2\2\2\u009c\u009e")
        buf.write("\5\22\n\2\u009d\u0098\3\2\2\2\u009d\u009c\3\2\2\2\u009e")
        buf.write("\21\3\2\2\2\u009f\u00a5\5\n\6\2\u00a0\u00a1\7\63\2\2\u00a1")
        buf.write("\u00a2\5\20\t\2\u00a2\u00a3\7\64\2\2\u00a3\u00a5\3\2\2")
        buf.write("\2\u00a4\u009f\3\2\2\2\u00a4\u00a0\3\2\2\2\u00a5\23\3")
        buf.write("\2\2\2\u00a6\u00a7\5\32\16\2\u00a7\u00a8\58\35\2\u00a8")
        buf.write("\25\3\2\2\2\u00a9\u00aa\7=\2\2\u00aa\u00ab\7\66\2\2\u00ab")
        buf.write("\u00ad\5X-\2\u00ac\u00ae\5p9\2\u00ad\u00ac\3\2\2\2\u00ad")
        buf.write("\u00ae\3\2\2\2\u00ae\u00b1\3\2\2\2\u00af\u00b0\7\62\2")
        buf.write("\2\u00b0\u00b2\5\26\f\2\u00b1\u00af\3\2\2\2\u00b1\u00b2")
        buf.write("\3\2\2\2\u00b2\u00ba\3\2\2\2\u00b3\u00b4\7=\2\2\u00b4")
        buf.write("\u00b6\7\63\2\2\u00b5\u00b7\5\26\f\2\u00b6\u00b5\3\2\2")
        buf.write("\2\u00b6\u00b7\3\2\2\2\u00b7\u00b8\3\2\2\2\u00b8\u00ba")
        buf.write("\7\64\2\2\u00b9\u00a9\3\2\2\2\u00b9\u00b3\3\2\2\2\u00ba")
        buf.write("\27\3\2\2\2\u00bb\u00bc\t\3\2\2\u00bc\u00bd\7=\2\2\u00bd")
        buf.write("\u00be\5\32\16\2\u00be\u00c1\58\35\2\u00bf\u00c0\7\"\2")
        buf.write("\2\u00c0\u00c2\5\16\b\2\u00c1\u00bf\3\2\2\2\u00c1\u00c2")
        buf.write("\3\2\2\2\u00c2\31\3\2\2\2\u00c3\u00c4\7.\2\2\u00c4\u00c5")
        buf.write("\5X-\2\u00c5\u00c7\7/\2\2\u00c6\u00c8\5\32\16\2\u00c7")
        buf.write("\u00c6\3\2\2\2\u00c7\u00c8\3\2\2\2\u00c8\33\3\2\2\2\u00c9")
        buf.write("\u00ca\t\4\2\2\u00ca\35\3\2\2\2\u00cb\u00cc\7=\2\2\u00cc")
        buf.write("\u00ce\7\60\2\2\u00cd\u00cf\5\62\32\2\u00ce\u00cd\3\2")
        buf.write("\2\2\u00ce\u00cf\3\2\2\2\u00cf\u00d0\3\2\2\2\u00d0\u00d1")
        buf.write("\7\61\2\2\u00d1\37\3\2\2\2\u00d2\u00d3\7\"\2\2\u00d3\u00d4")
        buf.write("\5X-\2\u00d4!\3\2\2\2\u00d5\u00d6\7\20\2\2\u00d6\u00dc")
        buf.write("\7=\2\2\u00d7\u00dd\58\35\2\u00d8\u00dd\5 \21\2\u00d9")
        buf.write("\u00da\58\35\2\u00da\u00db\5 \21\2\u00db\u00dd\3\2\2\2")
        buf.write("\u00dc\u00d7\3\2\2\2\u00dc\u00d8\3\2\2\2\u00dc\u00d9\3")
        buf.write("\2\2\2\u00dd#\3\2\2\2\u00de\u00df\7\17\2\2\u00df\u00e1")
        buf.write("\7=\2\2\u00e0\u00e2\58\35\2\u00e1\u00e0\3\2\2\2\u00e1")
        buf.write("\u00e2\3\2\2\2\u00e2\u00e3\3\2\2\2\u00e3\u00e4\5 \21\2")
        buf.write("\u00e4%\3\2\2\2\u00e5\u00e6\7\b\2\2\u00e6\u00e7\7=\2\2")
        buf.write("\u00e7\u00e9\7\t\2\2\u00e8\u00ea\5r:\2\u00e9\u00e8\3\2")
        buf.write("\2\2\u00e9\u00ea\3\2\2\2\u00ea\u00eb\3\2\2\2\u00eb\u00ed")
        buf.write("\7\63\2\2\u00ec\u00ee\5p9\2\u00ed\u00ec\3\2\2\2\u00ed")
        buf.write("\u00ee\3\2\2\2\u00ee\u00ef\3\2\2\2\u00ef\u00f0\5(\25\2")
        buf.write("\u00f0\u00f1\7\64\2\2\u00f1\'\3\2\2\2\u00f2\u00f3\7=\2")
        buf.write("\2\u00f3\u00f8\58\35\2\u00f4\u00f8\5&\24\2\u00f5\u00f8")
        buf.write("\5.\30\2\u00f6\u00f8\5*\26\2\u00f7\u00f2\3\2\2\2\u00f7")
        buf.write("\u00f4\3\2\2\2\u00f7\u00f5\3\2\2\2\u00f7\u00f6\3\2\2\2")
        buf.write("\u00f8\u00f9\3\2\2\2\u00f9\u00fb\5p9\2\u00fa\u00fc\5(")
        buf.write("\25\2\u00fb\u00fa\3\2\2\2\u00fb\u00fc\3\2\2\2\u00fc)\3")
        buf.write("\2\2\2\u00fd\u00fe\7\b\2\2\u00fe\u00ff\7=\2\2\u00ff\u0101")
        buf.write("\7\n\2\2\u0100\u0102\5r:\2\u0101\u0100\3\2\2\2\u0101\u0102")
        buf.write("\3\2\2\2\u0102\u0103\3\2\2\2\u0103\u0105\7\63\2\2\u0104")
        buf.write("\u0106\5p9\2\u0105\u0104\3\2\2\2\u0105\u0106\3\2\2\2\u0106")
        buf.write("\u0107\3\2\2\2\u0107\u0108\5,\27\2\u0108\u0109\7\64\2")
        buf.write("\2\u0109+\3\2\2\2\u010a\u010b\7=\2\2\u010b\u010d\7\60")
        buf.write("\2\2\u010c\u010e\5\60\31\2\u010d\u010c\3\2\2\2\u010d\u010e")
        buf.write("\3\2\2\2\u010e\u010f\3\2\2\2\u010f\u0111\7\61\2\2\u0110")
        buf.write("\u0112\58\35\2\u0111\u0110\3\2\2\2\u0111\u0112\3\2\2\2")
        buf.write("\u0112\u0113\3\2\2\2\u0113\u0115\5p9\2\u0114\u0116\5,")
        buf.write("\27\2\u0115\u0114\3\2\2\2\u0115\u0116\3\2\2\2\u0116-\3")
        buf.write("\2\2\2\u0117\u0118\7\7\2\2\u0118\u0119\7=\2\2\u0119\u011b")
        buf.write("\7\60\2\2\u011a\u011c\5\60\31\2\u011b\u011a\3\2\2\2\u011b")
        buf.write("\u011c\3\2\2\2\u011c\u011d\3\2\2\2\u011d\u011f\7\61\2")
        buf.write("\2\u011e\u0120\58\35\2\u011f\u011e\3\2\2\2\u011f\u0120")
        buf.write("\3\2\2\2\u0120\u0122\3\2\2\2\u0121\u0123\5r:\2\u0122\u0121")
        buf.write("\3\2\2\2\u0122\u0123\3\2\2\2\u0123\u0124\3\2\2\2\u0124")
        buf.write("\u0125\5D#\2\u0125/\3\2\2\2\u0126\u0127\5\66\34\2\u0127")
        buf.write("\u012a\58\35\2\u0128\u0129\7\62\2\2\u0129\u012b\5\60\31")
        buf.write("\2\u012a\u0128\3\2\2\2\u012a\u012b\3\2\2\2\u012b\61\3")
        buf.write("\2\2\2\u012c\u012e\5d\63\2\u012d\u012f\58\35\2\u012e\u012d")
        buf.write("\3\2\2\2\u012e\u012f\3\2\2\2\u012f\u0132\3\2\2\2\u0130")
        buf.write("\u0131\7\62\2\2\u0131\u0133\5\62\32\2\u0132\u0130\3\2")
        buf.write("\2\2\u0132\u0133\3\2\2\2\u0133\63\3\2\2\2\u0134\u0135")
        buf.write("\7\7\2\2\u0135\u0136\7\60\2\2\u0136\u0137\7=\2\2\u0137")
        buf.write("\u0138\7=\2\2\u0138\u0139\7\61\2\2\u0139\u013a\7=\2\2")
        buf.write("\u013a\u013c\7\60\2\2\u013b\u013d\5\60\31\2\u013c\u013b")
        buf.write("\3\2\2\2\u013c\u013d\3\2\2\2\u013d\u013e\3\2\2\2\u013e")
        buf.write("\u0140\7\61\2\2\u013f\u0141\58\35\2\u0140\u013f\3\2\2")
        buf.write("\2\u0140\u0141\3\2\2\2\u0141\u0143\3\2\2\2\u0142\u0144")
        buf.write("\5r:\2\u0143\u0142\3\2\2\2\u0143\u0144\3\2\2\2\u0144\u0145")
        buf.write("\3\2\2\2\u0145\u0146\5D#\2\u0146\65\3\2\2\2\u0147\u0148")
        buf.write("\7=\2\2\u0148\u0149\7\62\2\2\u0149\u014c\5\66\34\2\u014a")
        buf.write("\u014c\7=\2\2\u014b\u0147\3\2\2\2\u014b\u014a\3\2\2\2")
        buf.write("\u014c\67\3\2\2\2\u014d\u0151\5:\36\2\u014e\u0151\5\24")
        buf.write("\13\2\u014f\u0151\7=\2\2\u0150\u014d\3\2\2\2\u0150\u014e")
        buf.write("\3\2\2\2\u0150\u014f\3\2\2\2\u01519\3\2\2\2\u0152\u0153")
        buf.write("\t\5\2\2\u0153;\3\2\2\2\u0154\u0155\5> \2\u0155\u0156")
        buf.write("\5<\37\2\u0156\u0159\3\2\2\2\u0157\u0159\5> \2\u0158\u0154")
        buf.write("\3\2\2\2\u0158\u0157\3\2\2\2\u0159=\3\2\2\2\u015a\u0163")
        buf.write("\5\4\3\2\u015b\u0163\5@!\2\u015c\u0163\5F$\2\u015d\u0163")
        buf.write("\5J&\2\u015e\u0163\5P)\2\u015f\u0163\5R*\2\u0160\u0163")
        buf.write("\5T+\2\u0161\u0163\5B\"\2\u0162\u015a\3\2\2\2\u0162\u015b")
        buf.write("\3\2\2\2\u0162\u015c\3\2\2\2\u0162\u015d\3\2\2\2\u0162")
        buf.write("\u015e\3\2\2\2\u0162\u015f\3\2\2\2\u0162\u0160\3\2\2\2")
        buf.write("\u0162\u0161\3\2\2\2\u0163\u0164\3\2\2\2\u0164\u0165\5")
        buf.write("p9\2\u0165?\3\2\2\2\u0166\u0167\5l\67\2\u0167\u0168\5")
        buf.write("n8\2\u0168\u0169\5X-\2\u0169A\3\2\2\2\u016a\u016c\7\6")
        buf.write("\2\2\u016b\u016d\5X-\2\u016c\u016b\3\2\2\2\u016c\u016d")
        buf.write("\3\2\2\2\u016dC\3\2\2\2\u016e\u0170\7\63\2\2\u016f\u0171")
        buf.write("\5p9\2\u0170\u016f\3\2\2\2\u0170\u0171\3\2\2\2\u0171\u0173")
        buf.write("\3\2\2\2\u0172\u0174\5<\37\2\u0173\u0172\3\2\2\2\u0173")
        buf.write("\u0174\3\2\2\2\u0174\u0175\3\2\2\2\u0175\u0176\7\64\2")
        buf.write("\2\u0176E\3\2\2\2\u0177\u0178\7\3\2\2\u0178\u0179\7\60")
        buf.write("\2\2\u0179\u017a\5X-\2\u017a\u017c\7\61\2\2\u017b\u017d")
        buf.write("\5r:\2\u017c\u017b\3\2\2\2\u017c\u017d\3\2\2\2\u017d\u017e")
        buf.write("\3\2\2\2\u017e\u017f\5D#\2\u017f\u0185\5H%\2\u0180\u0182")
        buf.write("\7\4\2\2\u0181\u0183\5r:\2\u0182\u0181\3\2\2\2\u0182\u0183")
        buf.write("\3\2\2\2\u0183\u0184\3\2\2\2\u0184\u0186\5D#\2\u0185\u0180")
        buf.write("\3\2\2\2\u0185\u0186\3\2\2\2\u0186G\3\2\2\2\u0187\u0188")
        buf.write("\7\4\2\2\u0188\u0189\7\3\2\2\u0189\u018a\7\60\2\2\u018a")
        buf.write("\u018b\5X-\2\u018b\u018d\7\61\2\2\u018c\u018e\5r:\2\u018d")
        buf.write("\u018c\3\2\2\2\u018d\u018e\3\2\2\2\u018e\u018f\3\2\2\2")
        buf.write("\u018f\u0190\5D#\2\u0190\u0191\5H%\2\u0191\u0194\3\2\2")
        buf.write("\2\u0192\u0194\3\2\2\2\u0193\u0187\3\2\2\2\u0193\u0192")
        buf.write("\3\2\2\2\u0194I\3\2\2\2\u0195\u0198\5L\'\2\u0196\u0198")
        buf.write("\5N(\2\u0197\u0195\3\2\2\2\u0197\u0196\3\2\2\2\u0198K")
        buf.write("\3\2\2\2\u0199\u019a\7\5\2\2\u019a\u019b\7=\2\2\u019b")
        buf.write("\u019c\7\62\2\2\u019c\u019d\7=\2\2\u019d\u019e\7%\2\2")
        buf.write("\u019e\u019f\7\23\2\2\u019f\u01a1\5d\63\2\u01a0\u01a2")
        buf.write("\5r:\2\u01a1\u01a0\3\2\2\2\u01a1\u01a2\3\2\2\2\u01a2\u01a3")
        buf.write("\3\2\2\2\u01a3\u01a4\5D#\2\u01a4M\3\2\2\2\u01a5\u01b8")
        buf.write("\7\5\2\2\u01a6\u01b9\5X-\2\u01a7\u01b0\5@!\2\u01a8\u01a9")
        buf.write("\7\20\2\2\u01a9\u01ab\7=\2\2\u01aa\u01ac\58\35\2\u01ab")
        buf.write("\u01aa\3\2\2\2\u01ab\u01ac\3\2\2\2\u01ac\u01ad\3\2\2\2")
        buf.write("\u01ad\u01ae\7\"\2\2\u01ae\u01b0\5X-\2\u01af\u01a7\3\2")
        buf.write("\2\2\u01af\u01a8\3\2\2\2\u01b0\u01b1\3\2\2\2\u01b1\u01b2")
        buf.write("\5p9\2\u01b2\u01b3\5X-\2\u01b3\u01b4\5p9\2\u01b4\u01b5")
        buf.write("\7=\2\2\u01b5\u01b6\5n8\2\u01b6\u01b7\5X-\2\u01b7\u01b9")
        buf.write("\3\2\2\2\u01b8\u01a6\3\2\2\2\u01b8\u01af\3\2\2\2\u01b9")
        buf.write("\u01ba\3\2\2\2\u01ba\u01bb\5D#\2\u01bbO\3\2\2\2\u01bc")
        buf.write("\u01bd\7\22\2\2\u01bdQ\3\2\2\2\u01be\u01bf\7\21\2\2\u01bf")
        buf.write("S\3\2\2\2\u01c0\u01c1\5d\63\2\u01c1\u01c3\7\60\2\2\u01c2")
        buf.write("\u01c4\5V,\2\u01c3\u01c2\3\2\2\2\u01c3\u01c4\3\2\2\2\u01c4")
        buf.write("\u01c5\3\2\2\2\u01c5\u01c6\7\61\2\2\u01c6U\3\2\2\2\u01c7")
        buf.write("\u01c8\5X-\2\u01c8\u01c9\7\62\2\2\u01c9\u01ca\5V,\2\u01ca")
        buf.write("\u01cd\3\2\2\2\u01cb\u01cd\5X-\2\u01cc\u01c7\3\2\2\2\u01cc")
        buf.write("\u01cb\3\2\2\2\u01cdW\3\2\2\2\u01ce\u01cf\b-\1\2\u01cf")
        buf.write("\u01d0\5Z.\2\u01d0\u01d6\3\2\2\2\u01d1\u01d2\f\4\2\2\u01d2")
        buf.write("\u01d3\7,\2\2\u01d3\u01d5\5Z.\2\u01d4\u01d1\3\2\2\2\u01d5")
        buf.write("\u01d8\3\2\2\2\u01d6\u01d4\3\2\2\2\u01d6\u01d7\3\2\2\2")
        buf.write("\u01d7Y\3\2\2\2\u01d8\u01d6\3\2\2\2\u01d9\u01da\b.\1\2")
        buf.write("\u01da\u01db\5\\/\2\u01db\u01e1\3\2\2\2\u01dc\u01dd\f")
        buf.write("\4\2\2\u01dd\u01de\7-\2\2\u01de\u01e0\5\\/\2\u01df\u01dc")
        buf.write("\3\2\2\2\u01e0\u01e3\3\2\2\2\u01e1\u01df\3\2\2\2\u01e1")
        buf.write("\u01e2\3\2\2\2\u01e2[\3\2\2\2\u01e3\u01e1\3\2\2\2\u01e4")
        buf.write("\u01e5\b/\1\2\u01e5\u01e6\5^\60\2\u01e6\u01ec\3\2\2\2")
        buf.write("\u01e7\u01e8\f\4\2\2\u01e8\u01e9\t\6\2\2\u01e9\u01eb\5")
        buf.write("^\60\2\u01ea\u01e7\3\2\2\2\u01eb\u01ee\3\2\2\2\u01ec\u01ea")
        buf.write("\3\2\2\2\u01ec\u01ed\3\2\2\2\u01ed]\3\2\2\2\u01ee\u01ec")
        buf.write("\3\2\2\2\u01ef\u01f0\b\60\1\2\u01f0\u01f1\5`\61\2\u01f1")
        buf.write("\u01f7\3\2\2\2\u01f2\u01f3\f\4\2\2\u01f3\u01f4\t\7\2\2")
        buf.write("\u01f4\u01f6\5`\61\2\u01f5\u01f2\3\2\2\2\u01f6\u01f9\3")
        buf.write("\2\2\2\u01f7\u01f5\3\2\2\2\u01f7\u01f8\3\2\2\2\u01f8_")
        buf.write("\3\2\2\2\u01f9\u01f7\3\2\2\2\u01fa\u01fb\b\61\1\2\u01fb")
        buf.write("\u01fc\5b\62\2\u01fc\u0202\3\2\2\2\u01fd\u01fe\f\4\2\2")
        buf.write("\u01fe\u01ff\t\b\2\2\u01ff\u0201\5b\62\2\u0200\u01fd\3")
        buf.write("\2\2\2\u0201\u0204\3\2\2\2\u0202\u0200\3\2\2\2\u0202\u0203")
        buf.write("\3\2\2\2\u0203a\3\2\2\2\u0204\u0202\3\2\2\2\u0205\u0206")
        buf.write("\t\t\2\2\u0206\u0209\5b\62\2\u0207\u0209\5d\63\2\u0208")
        buf.write("\u0205\3\2\2\2\u0208\u0207\3\2\2\2\u0209c\3\2\2\2\u020a")
        buf.write("\u020b\b\63\1\2\u020b\u020c\5f\64\2\u020c\u021d\3\2\2")
        buf.write("\2\u020d\u020e\f\7\2\2\u020e\u0210\7\63\2\2\u020f\u0211")
        buf.write("\5X-\2\u0210\u020f\3\2\2\2\u0210\u0211\3\2\2\2\u0211\u0212")
        buf.write("\3\2\2\2\u0212\u021c\7\64\2\2\u0213\u0214\f\6\2\2\u0214")
        buf.write("\u0215\7$\2\2\u0215\u021c\7=\2\2\u0216\u0217\f\5\2\2\u0217")
        buf.write("\u0218\7$\2\2\u0218\u021c\5h\65\2\u0219\u021a\f\4\2\2")
        buf.write("\u021a\u021c\5\32\16\2\u021b\u020d\3\2\2\2\u021b\u0213")
        buf.write("\3\2\2\2\u021b\u0216\3\2\2\2\u021b\u0219\3\2\2\2\u021c")
        buf.write("\u021f\3\2\2\2\u021d\u021b\3\2\2\2\u021d\u021e\3\2\2\2")
        buf.write("\u021ee\3\2\2\2\u021f\u021d\3\2\2\2\u0220\u0228\7=\2\2")
        buf.write("\u0221\u0228\5\n\6\2\u0222\u0228\5h\65\2\u0223\u0224\7")
        buf.write("\60\2\2\u0224\u0225\5X-\2\u0225\u0226\7\61\2\2\u0226\u0228")
        buf.write("\3\2\2\2\u0227\u0220\3\2\2\2\u0227\u0221\3\2\2\2\u0227")
        buf.write("\u0222\3\2\2\2\u0227\u0223\3\2\2\2\u0228g\3\2\2\2\u0229")
        buf.write("\u022a\7=\2\2\u022a\u022c\7\60\2\2\u022b\u022d\5V,\2\u022c")
        buf.write("\u022b\3\2\2\2\u022c\u022d\3\2\2\2\u022d\u022e\3\2\2\2")
        buf.write("\u022e\u022f\7\61\2\2\u022fi\3\2\2\2\u0230\u0233\7=\2")
        buf.write("\2\u0231\u0233\5h\65\2\u0232\u0230\3\2\2\2\u0232\u0231")
        buf.write("\3\2\2\2\u0233k\3\2\2\2\u0234\u0235\b\67\1\2\u0235\u0236")
        buf.write("\5j\66\2\u0236\u023e\3\2\2\2\u0237\u0238\f\5\2\2\u0238")
        buf.write("\u0239\7$\2\2\u0239\u023d\5j\66\2\u023a\u023b\f\4\2\2")
        buf.write("\u023b\u023d\5\32\16\2\u023c\u0237\3\2\2\2\u023c\u023a")
        buf.write("\3\2\2\2\u023d\u0240\3\2\2\2\u023e\u023c\3\2\2\2\u023e")
        buf.write("\u023f\3\2\2\2\u023fm\3\2\2\2\u0240\u023e\3\2\2\2\u0241")
        buf.write("\u0242\t\n\2\2\u0242o\3\2\2\2\u0243\u0245\t\13\2\2\u0244")
        buf.write("\u0246\5p9\2\u0245\u0244\3\2\2\2\u0245\u0246\3\2\2\2\u0246")
        buf.write("q\3\2\2\2\u0247\u0249\7A\2\2\u0248\u024a\5r:\2\u0249\u0248")
        buf.write("\3\2\2\2\u0249\u024a\3\2\2\2\u024as\3\2\2\2Fu\u0081\u008a")
        buf.write("\u008f\u009d\u00a4\u00ad\u00b1\u00b6\u00b9\u00c1\u00c7")
        buf.write("\u00ce\u00dc\u00e1\u00e9\u00ed\u00f7\u00fb\u0101\u0105")
        buf.write("\u010d\u0111\u0115\u011b\u011f\u0122\u012a\u012e\u0132")
        buf.write("\u013c\u0140\u0143\u014b\u0150\u0158\u0162\u016c\u0170")
        buf.write("\u0173\u017c\u0182\u0185\u018d\u0193\u0197\u01a1\u01ab")
        buf.write("\u01af\u01b8\u01c3\u01cc\u01d6\u01e1\u01ec\u01f7\u0202")
        buf.write("\u0208\u0210\u021b\u021d\u0227\u022c\u0232\u023c\u023e")
        buf.write("\u0245\u0249")
        return buf.getvalue()


class MiniGoParser ( Parser ):

    grammarFileName = "MiniGo.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'if'", "'else'", "'for'", "'return'", 
                     "'func'", "'type'", "'struct'", "'interface'", "<INVALID>", 
                     "'int'", "'float'", "'boolean'", "'const'", "'var'", 
                     "'continue'", "'break'", "'range'", "'nil'", "'true'", 
                     "'false'", "'+'", "'-'", "'*'", "'/'", "'%'", "'=='", 
                     "'!='", "'<'", "'>'", "'<='", "'>='", "'='", "'**'", 
                     "'.'", "':='", "'/='", "'%='", "'+='", "'-='", "'*='", 
                     "'!'", "'||'", "'&&'", "'['", "']'", "'('", "')'", 
                     "','", "'{'", "'}'", "';'", "':'" ]

    symbolicNames = [ "<INVALID>", "IF", "ELSE", "FOR", "RETURN", "FUNC", 
                      "TYPE", "STRUCT", "INTERFACE", "STRING", "INT", "FLOAT", 
                      "BOOLEAN", "CONST", "VAR", "CONTINUE", "BREAK", "RANGE", 
                      "NIL", "TRUE", "FALSE", "ADD", "SUB", "MUL", "DIV", 
                      "MOD", "EQ", "NEQ", "LT", "GT", "LTE", "GTE", "ASSIGNINIT", 
                      "EXP", "DOT", "ASSIGN", "E_DIV", "E_MOD", "E_ADD", 
                      "E_SUB", "E_MUL", "NOT", "OR", "AND", "LSB", "RSB", 
                      "LP", "RP", "CM", "LCB", "RCB", "SC", "CO", "INT_LIT", 
                      "FLOAT_LIT", "HEX_LIT", "BI_LIT", "OCT_LIT", "BOOL_LIT", 
                      "ID", "STRING_LIT", "COMMENT_LINE", "COMMENT", "NEWLINE", 
                      "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    RULE_program = 0
    RULE_declared_statement = 1
    RULE_declared = 2
    RULE_list_declared = 3
    RULE_literal = 4
    RULE_primitive_literal = 5
    RULE_array_literal = 6
    RULE_array = 7
    RULE_array_list = 8
    RULE_array_type = 9
    RULE_struct_literal = 10
    RULE_array_declared = 11
    RULE_array_dimension = 12
    RULE_number = 13
    RULE_func_literal = 14
    RULE_variables_init = 15
    RULE_variables_declared = 16
    RULE_constants_declared = 17
    RULE_struct_declared = 18
    RULE_struct_field = 19
    RULE_interface_declared = 20
    RULE_interface_method = 21
    RULE_function_declared = 22
    RULE_para_declare = 23
    RULE_para_list = 24
    RULE_method_declared = 25
    RULE_list_identifiers = 26
    RULE_types_specifier = 27
    RULE_basic_type = 28
    RULE_list_statement = 29
    RULE_statement = 30
    RULE_assign_statement = 31
    RULE_return_statement = 32
    RULE_block_statement = 33
    RULE_if_statement = 34
    RULE_else_if = 35
    RULE_for_statement = 36
    RULE_range_for = 37
    RULE_index_for = 38
    RULE_break_statement = 39
    RULE_continue_statement = 40
    RULE_call_statement = 41
    RULE_list_expression = 42
    RULE_expression = 43
    RULE_expression1 = 44
    RULE_expression2 = 45
    RULE_expression3 = 46
    RULE_expression4 = 47
    RULE_expression5 = 48
    RULE_expression6 = 49
    RULE_expression7 = 50
    RULE_funtion_call = 51
    RULE_var_check = 52
    RULE_nolit = 53
    RULE_assign = 54
    RULE_stmtend = 55
    RULE_ignore = 56

    ruleNames =  [ "program", "declared_statement", "declared", "list_declared", 
                   "literal", "primitive_literal", "array_literal", "array", 
                   "array_list", "array_type", "struct_literal", "array_declared", 
                   "array_dimension", "number", "func_literal", "variables_init", 
                   "variables_declared", "constants_declared", "struct_declared", 
                   "struct_field", "interface_declared", "interface_method", 
                   "function_declared", "para_declare", "para_list", "method_declared", 
                   "list_identifiers", "types_specifier", "basic_type", 
                   "list_statement", "statement", "assign_statement", "return_statement", 
                   "block_statement", "if_statement", "else_if", "for_statement", 
                   "range_for", "index_for", "break_statement", "continue_statement", 
                   "call_statement", "list_expression", "expression", "expression1", 
                   "expression2", "expression3", "expression4", "expression5", 
                   "expression6", "expression7", "funtion_call", "var_check", 
                   "nolit", "assign", "stmtend", "ignore" ]

    EOF = Token.EOF
    IF=1
    ELSE=2
    FOR=3
    RETURN=4
    FUNC=5
    TYPE=6
    STRUCT=7
    INTERFACE=8
    STRING=9
    INT=10
    FLOAT=11
    BOOLEAN=12
    CONST=13
    VAR=14
    CONTINUE=15
    BREAK=16
    RANGE=17
    NIL=18
    TRUE=19
    FALSE=20
    ADD=21
    SUB=22
    MUL=23
    DIV=24
    MOD=25
    EQ=26
    NEQ=27
    LT=28
    GT=29
    LTE=30
    GTE=31
    ASSIGNINIT=32
    EXP=33
    DOT=34
    ASSIGN=35
    E_DIV=36
    E_MOD=37
    E_ADD=38
    E_SUB=39
    E_MUL=40
    NOT=41
    OR=42
    AND=43
    LSB=44
    RSB=45
    LP=46
    RP=47
    CM=48
    LCB=49
    RCB=50
    SC=51
    CO=52
    INT_LIT=53
    FLOAT_LIT=54
    HEX_LIT=55
    BI_LIT=56
    OCT_LIT=57
    BOOL_LIT=58
    ID=59
    STRING_LIT=60
    COMMENT_LINE=61
    COMMENT=62
    NEWLINE=63
    WS=64
    ERROR_CHAR=65
    UNCLOSE_STRING=66
    ILLEGAL_ESCAPE=67

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def list_declared(self):
            return self.getTypedRuleContext(MiniGoParser.List_declaredContext,0)


        def EOF(self):
            return self.getToken(MiniGoParser.EOF, 0)

        def stmtend(self):
            return self.getTypedRuleContext(MiniGoParser.StmtendContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = MiniGoParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 115
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.SC or _la==MiniGoParser.NEWLINE:
                self.state = 114
                self.stmtend()


            self.state = 117
            self.list_declared()
            self.state = 118
            self.match(MiniGoParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Declared_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variables_declared(self):
            return self.getTypedRuleContext(MiniGoParser.Variables_declaredContext,0)


        def constants_declared(self):
            return self.getTypedRuleContext(MiniGoParser.Constants_declaredContext,0)


        def struct_declared(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_declaredContext,0)


        def array_declared(self):
            return self.getTypedRuleContext(MiniGoParser.Array_declaredContext,0)


        def function_declared(self):
            return self.getTypedRuleContext(MiniGoParser.Function_declaredContext,0)


        def interface_declared(self):
            return self.getTypedRuleContext(MiniGoParser.Interface_declaredContext,0)


        def method_declared(self):
            return self.getTypedRuleContext(MiniGoParser.Method_declaredContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_declared_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclared_statement" ):
                return visitor.visitDeclared_statement(self)
            else:
                return visitor.visitChildren(self)




    def declared_statement(self):

        localctx = MiniGoParser.Declared_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_declared_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 127
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.state = 120
                self.variables_declared()
                pass

            elif la_ == 2:
                self.state = 121
                self.constants_declared()
                pass

            elif la_ == 3:
                self.state = 122
                self.struct_declared()
                pass

            elif la_ == 4:
                self.state = 123
                self.array_declared()
                pass

            elif la_ == 5:
                self.state = 124
                self.function_declared()
                pass

            elif la_ == 6:
                self.state = 125
                self.interface_declared()
                pass

            elif la_ == 7:
                self.state = 126
                self.method_declared()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclaredContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declared_statement(self):
            return self.getTypedRuleContext(MiniGoParser.Declared_statementContext,0)


        def stmtend(self):
            return self.getTypedRuleContext(MiniGoParser.StmtendContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_declared

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclared" ):
                return visitor.visitDeclared(self)
            else:
                return visitor.visitChildren(self)




    def declared(self):

        localctx = MiniGoParser.DeclaredContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_declared)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 129
            self.declared_statement()
            self.state = 130
            self.stmtend()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_declaredContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declared(self):
            return self.getTypedRuleContext(MiniGoParser.DeclaredContext,0)


        def list_declared(self):
            return self.getTypedRuleContext(MiniGoParser.List_declaredContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_list_declared

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_declared" ):
                return visitor.visitList_declared(self)
            else:
                return visitor.visitChildren(self)




    def list_declared(self):

        localctx = MiniGoParser.List_declaredContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_list_declared)
        try:
            self.state = 136
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 132
                self.declared()
                self.state = 133
                self.list_declared()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 135
                self.declared()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primitive_literal(self):
            return self.getTypedRuleContext(MiniGoParser.Primitive_literalContext,0)


        def array_literal(self):
            return self.getTypedRuleContext(MiniGoParser.Array_literalContext,0)


        def struct_literal(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_literalContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = MiniGoParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_literal)
        try:
            self.state = 141
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.NIL, MiniGoParser.TRUE, MiniGoParser.FALSE, MiniGoParser.INT_LIT, MiniGoParser.FLOAT_LIT, MiniGoParser.HEX_LIT, MiniGoParser.BI_LIT, MiniGoParser.OCT_LIT, MiniGoParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 138
                self.primitive_literal()
                pass
            elif token in [MiniGoParser.LSB]:
                self.enterOuterAlt(localctx, 2)
                self.state = 139
                self.array_literal()
                pass
            elif token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 3)
                self.state = 140
                self.struct_literal()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Primitive_literalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT_LIT(self):
            return self.getToken(MiniGoParser.INT_LIT, 0)

        def FLOAT_LIT(self):
            return self.getToken(MiniGoParser.FLOAT_LIT, 0)

        def TRUE(self):
            return self.getToken(MiniGoParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(MiniGoParser.FALSE, 0)

        def STRING_LIT(self):
            return self.getToken(MiniGoParser.STRING_LIT, 0)

        def HEX_LIT(self):
            return self.getToken(MiniGoParser.HEX_LIT, 0)

        def OCT_LIT(self):
            return self.getToken(MiniGoParser.OCT_LIT, 0)

        def BI_LIT(self):
            return self.getToken(MiniGoParser.BI_LIT, 0)

        def NIL(self):
            return self.getToken(MiniGoParser.NIL, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_primitive_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimitive_literal" ):
                return visitor.visitPrimitive_literal(self)
            else:
                return visitor.visitChildren(self)




    def primitive_literal(self):

        localctx = MiniGoParser.Primitive_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_primitive_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 143
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.NIL) | (1 << MiniGoParser.TRUE) | (1 << MiniGoParser.FALSE) | (1 << MiniGoParser.INT_LIT) | (1 << MiniGoParser.FLOAT_LIT) | (1 << MiniGoParser.HEX_LIT) | (1 << MiniGoParser.BI_LIT) | (1 << MiniGoParser.OCT_LIT) | (1 << MiniGoParser.STRING_LIT))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_literalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def array_type(self):
            return self.getTypedRuleContext(MiniGoParser.Array_typeContext,0)


        def LCB(self):
            return self.getToken(MiniGoParser.LCB, 0)

        def array(self):
            return self.getTypedRuleContext(MiniGoParser.ArrayContext,0)


        def RCB(self):
            return self.getToken(MiniGoParser.RCB, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_array_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_literal" ):
                return visitor.visitArray_literal(self)
            else:
                return visitor.visitChildren(self)




    def array_literal(self):

        localctx = MiniGoParser.Array_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_array_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 145
            self.array_type()
            self.state = 146
            self.match(MiniGoParser.LCB)
            self.state = 147
            self.array()
            self.state = 148
            self.match(MiniGoParser.RCB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def array_list(self):
            return self.getTypedRuleContext(MiniGoParser.Array_listContext,0)


        def CM(self):
            return self.getToken(MiniGoParser.CM, 0)

        def array(self):
            return self.getTypedRuleContext(MiniGoParser.ArrayContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_array

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray" ):
                return visitor.visitArray(self)
            else:
                return visitor.visitChildren(self)




    def array(self):

        localctx = MiniGoParser.ArrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_array)
        try:
            self.state = 155
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 150
                self.array_list()
                self.state = 151
                self.match(MiniGoParser.CM)
                self.state = 152
                self.array()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 154
                self.array_list()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literal(self):
            return self.getTypedRuleContext(MiniGoParser.LiteralContext,0)


        def LCB(self):
            return self.getToken(MiniGoParser.LCB, 0)

        def array(self):
            return self.getTypedRuleContext(MiniGoParser.ArrayContext,0)


        def RCB(self):
            return self.getToken(MiniGoParser.RCB, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_array_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_list" ):
                return visitor.visitArray_list(self)
            else:
                return visitor.visitChildren(self)




    def array_list(self):

        localctx = MiniGoParser.Array_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_array_list)
        try:
            self.state = 162
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.NIL, MiniGoParser.TRUE, MiniGoParser.FALSE, MiniGoParser.LSB, MiniGoParser.INT_LIT, MiniGoParser.FLOAT_LIT, MiniGoParser.HEX_LIT, MiniGoParser.BI_LIT, MiniGoParser.OCT_LIT, MiniGoParser.ID, MiniGoParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 157
                self.literal()
                pass
            elif token in [MiniGoParser.LCB]:
                self.enterOuterAlt(localctx, 2)
                self.state = 158
                self.match(MiniGoParser.LCB)
                self.state = 159
                self.array()
                self.state = 160
                self.match(MiniGoParser.RCB)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def array_dimension(self):
            return self.getTypedRuleContext(MiniGoParser.Array_dimensionContext,0)


        def types_specifier(self):
            return self.getTypedRuleContext(MiniGoParser.Types_specifierContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_array_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_type" ):
                return visitor.visitArray_type(self)
            else:
                return visitor.visitChildren(self)




    def array_type(self):

        localctx = MiniGoParser.Array_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_array_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 164
            self.array_dimension()
            self.state = 165
            self.types_specifier()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Struct_literalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def CO(self):
            return self.getToken(MiniGoParser.CO, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def stmtend(self):
            return self.getTypedRuleContext(MiniGoParser.StmtendContext,0)


        def CM(self):
            return self.getToken(MiniGoParser.CM, 0)

        def struct_literal(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_literalContext,0)


        def LCB(self):
            return self.getToken(MiniGoParser.LCB, 0)

        def RCB(self):
            return self.getToken(MiniGoParser.RCB, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct_literal" ):
                return visitor.visitStruct_literal(self)
            else:
                return visitor.visitChildren(self)




    def struct_literal(self):

        localctx = MiniGoParser.Struct_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_struct_literal)
        self._la = 0 # Token type
        try:
            self.state = 183
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 167
                self.match(MiniGoParser.ID)
                self.state = 168
                self.match(MiniGoParser.CO)
                self.state = 169
                self.expression(0)
                self.state = 171
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
                if la_ == 1:
                    self.state = 170
                    self.stmtend()


                self.state = 175
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
                if la_ == 1:
                    self.state = 173
                    self.match(MiniGoParser.CM)
                    self.state = 174
                    self.struct_literal()


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 177
                self.match(MiniGoParser.ID)
                self.state = 178
                self.match(MiniGoParser.LCB)
                self.state = 180
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==MiniGoParser.ID:
                    self.state = 179
                    self.struct_literal()


                self.state = 182
                self.match(MiniGoParser.RCB)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_declaredContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def array_dimension(self):
            return self.getTypedRuleContext(MiniGoParser.Array_dimensionContext,0)


        def types_specifier(self):
            return self.getTypedRuleContext(MiniGoParser.Types_specifierContext,0)


        def CONST(self):
            return self.getToken(MiniGoParser.CONST, 0)

        def VAR(self):
            return self.getToken(MiniGoParser.VAR, 0)

        def ASSIGNINIT(self):
            return self.getToken(MiniGoParser.ASSIGNINIT, 0)

        def array_literal(self):
            return self.getTypedRuleContext(MiniGoParser.Array_literalContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_array_declared

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_declared" ):
                return visitor.visitArray_declared(self)
            else:
                return visitor.visitChildren(self)




    def array_declared(self):

        localctx = MiniGoParser.Array_declaredContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_array_declared)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 185
            _la = self._input.LA(1)
            if not(_la==MiniGoParser.CONST or _la==MiniGoParser.VAR):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 186
            self.match(MiniGoParser.ID)
            self.state = 187
            self.array_dimension()
            self.state = 188
            self.types_specifier()
            self.state = 191
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.ASSIGNINIT:
                self.state = 189
                self.match(MiniGoParser.ASSIGNINIT)
                self.state = 190
                self.array_literal()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_dimensionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LSB(self):
            return self.getToken(MiniGoParser.LSB, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def RSB(self):
            return self.getToken(MiniGoParser.RSB, 0)

        def array_dimension(self):
            return self.getTypedRuleContext(MiniGoParser.Array_dimensionContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_array_dimension

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_dimension" ):
                return visitor.visitArray_dimension(self)
            else:
                return visitor.visitChildren(self)




    def array_dimension(self):

        localctx = MiniGoParser.Array_dimensionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_array_dimension)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 193
            self.match(MiniGoParser.LSB)
            self.state = 194
            self.expression(0)
            self.state = 195
            self.match(MiniGoParser.RSB)
            self.state = 197
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.state = 196
                self.array_dimension()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NumberContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT_LIT(self):
            return self.getToken(MiniGoParser.INT_LIT, 0)

        def HEX_LIT(self):
            return self.getToken(MiniGoParser.HEX_LIT, 0)

        def OCT_LIT(self):
            return self.getToken(MiniGoParser.OCT_LIT, 0)

        def BI_LIT(self):
            return self.getToken(MiniGoParser.BI_LIT, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_number

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumber" ):
                return visitor.visitNumber(self)
            else:
                return visitor.visitChildren(self)




    def number(self):

        localctx = MiniGoParser.NumberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_number)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 199
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.INT_LIT) | (1 << MiniGoParser.HEX_LIT) | (1 << MiniGoParser.BI_LIT) | (1 << MiniGoParser.OCT_LIT))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_literalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def LP(self):
            return self.getToken(MiniGoParser.LP, 0)

        def RP(self):
            return self.getToken(MiniGoParser.RP, 0)

        def para_list(self):
            return self.getTypedRuleContext(MiniGoParser.Para_listContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_func_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_literal" ):
                return visitor.visitFunc_literal(self)
            else:
                return visitor.visitChildren(self)




    def func_literal(self):

        localctx = MiniGoParser.Func_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_func_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 201
            self.match(MiniGoParser.ID)
            self.state = 202
            self.match(MiniGoParser.LP)
            self.state = 204
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.NIL) | (1 << MiniGoParser.TRUE) | (1 << MiniGoParser.FALSE) | (1 << MiniGoParser.LSB) | (1 << MiniGoParser.LP) | (1 << MiniGoParser.INT_LIT) | (1 << MiniGoParser.FLOAT_LIT) | (1 << MiniGoParser.HEX_LIT) | (1 << MiniGoParser.BI_LIT) | (1 << MiniGoParser.OCT_LIT) | (1 << MiniGoParser.ID) | (1 << MiniGoParser.STRING_LIT))) != 0):
                self.state = 203
                self.para_list()


            self.state = 206
            self.match(MiniGoParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Variables_initContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ASSIGNINIT(self):
            return self.getToken(MiniGoParser.ASSIGNINIT, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_variables_init

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariables_init" ):
                return visitor.visitVariables_init(self)
            else:
                return visitor.visitChildren(self)




    def variables_init(self):

        localctx = MiniGoParser.Variables_initContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_variables_init)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 208
            self.match(MiniGoParser.ASSIGNINIT)
            self.state = 209
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Variables_declaredContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(MiniGoParser.VAR, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def types_specifier(self):
            return self.getTypedRuleContext(MiniGoParser.Types_specifierContext,0)


        def variables_init(self):
            return self.getTypedRuleContext(MiniGoParser.Variables_initContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_variables_declared

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariables_declared" ):
                return visitor.visitVariables_declared(self)
            else:
                return visitor.visitChildren(self)




    def variables_declared(self):

        localctx = MiniGoParser.Variables_declaredContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_variables_declared)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 211
            self.match(MiniGoParser.VAR)
            self.state = 212
            self.match(MiniGoParser.ID)
            self.state = 218
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.state = 213
                self.types_specifier()
                pass

            elif la_ == 2:
                self.state = 214
                self.variables_init()
                pass

            elif la_ == 3:
                self.state = 215
                self.types_specifier()
                self.state = 216
                self.variables_init()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Constants_declaredContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONST(self):
            return self.getToken(MiniGoParser.CONST, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def variables_init(self):
            return self.getTypedRuleContext(MiniGoParser.Variables_initContext,0)


        def types_specifier(self):
            return self.getTypedRuleContext(MiniGoParser.Types_specifierContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_constants_declared

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstants_declared" ):
                return visitor.visitConstants_declared(self)
            else:
                return visitor.visitChildren(self)




    def constants_declared(self):

        localctx = MiniGoParser.Constants_declaredContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_constants_declared)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 220
            self.match(MiniGoParser.CONST)
            self.state = 221
            self.match(MiniGoParser.ID)
            self.state = 223
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.LSB) | (1 << MiniGoParser.ID))) != 0):
                self.state = 222
                self.types_specifier()


            self.state = 225
            self.variables_init()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Struct_declaredContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TYPE(self):
            return self.getToken(MiniGoParser.TYPE, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def STRUCT(self):
            return self.getToken(MiniGoParser.STRUCT, 0)

        def LCB(self):
            return self.getToken(MiniGoParser.LCB, 0)

        def struct_field(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_fieldContext,0)


        def RCB(self):
            return self.getToken(MiniGoParser.RCB, 0)

        def ignore(self):
            return self.getTypedRuleContext(MiniGoParser.IgnoreContext,0)


        def stmtend(self):
            return self.getTypedRuleContext(MiniGoParser.StmtendContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_declared

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct_declared" ):
                return visitor.visitStruct_declared(self)
            else:
                return visitor.visitChildren(self)




    def struct_declared(self):

        localctx = MiniGoParser.Struct_declaredContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_struct_declared)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 227
            self.match(MiniGoParser.TYPE)
            self.state = 228
            self.match(MiniGoParser.ID)
            self.state = 229
            self.match(MiniGoParser.STRUCT)
            self.state = 231
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.NEWLINE:
                self.state = 230
                self.ignore()


            self.state = 233
            self.match(MiniGoParser.LCB)
            self.state = 235
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.SC or _la==MiniGoParser.NEWLINE:
                self.state = 234
                self.stmtend()


            self.state = 237
            self.struct_field()
            self.state = 238
            self.match(MiniGoParser.RCB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Struct_fieldContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmtend(self):
            return self.getTypedRuleContext(MiniGoParser.StmtendContext,0)


        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def types_specifier(self):
            return self.getTypedRuleContext(MiniGoParser.Types_specifierContext,0)


        def struct_declared(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_declaredContext,0)


        def function_declared(self):
            return self.getTypedRuleContext(MiniGoParser.Function_declaredContext,0)


        def interface_declared(self):
            return self.getTypedRuleContext(MiniGoParser.Interface_declaredContext,0)


        def struct_field(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_fieldContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_field

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct_field" ):
                return visitor.visitStruct_field(self)
            else:
                return visitor.visitChildren(self)




    def struct_field(self):

        localctx = MiniGoParser.Struct_fieldContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_struct_field)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 245
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.state = 240
                self.match(MiniGoParser.ID)
                self.state = 241
                self.types_specifier()
                pass

            elif la_ == 2:
                self.state = 242
                self.struct_declared()
                pass

            elif la_ == 3:
                self.state = 243
                self.function_declared()
                pass

            elif la_ == 4:
                self.state = 244
                self.interface_declared()
                pass


            self.state = 247
            self.stmtend()
            self.state = 249
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.FUNC) | (1 << MiniGoParser.TYPE) | (1 << MiniGoParser.ID))) != 0):
                self.state = 248
                self.struct_field()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Interface_declaredContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TYPE(self):
            return self.getToken(MiniGoParser.TYPE, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def INTERFACE(self):
            return self.getToken(MiniGoParser.INTERFACE, 0)

        def LCB(self):
            return self.getToken(MiniGoParser.LCB, 0)

        def interface_method(self):
            return self.getTypedRuleContext(MiniGoParser.Interface_methodContext,0)


        def RCB(self):
            return self.getToken(MiniGoParser.RCB, 0)

        def ignore(self):
            return self.getTypedRuleContext(MiniGoParser.IgnoreContext,0)


        def stmtend(self):
            return self.getTypedRuleContext(MiniGoParser.StmtendContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_interface_declared

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInterface_declared" ):
                return visitor.visitInterface_declared(self)
            else:
                return visitor.visitChildren(self)




    def interface_declared(self):

        localctx = MiniGoParser.Interface_declaredContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_interface_declared)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 251
            self.match(MiniGoParser.TYPE)
            self.state = 252
            self.match(MiniGoParser.ID)
            self.state = 253
            self.match(MiniGoParser.INTERFACE)
            self.state = 255
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.NEWLINE:
                self.state = 254
                self.ignore()


            self.state = 257
            self.match(MiniGoParser.LCB)
            self.state = 259
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.SC or _la==MiniGoParser.NEWLINE:
                self.state = 258
                self.stmtend()


            self.state = 261
            self.interface_method()
            self.state = 262
            self.match(MiniGoParser.RCB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Interface_methodContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def LP(self):
            return self.getToken(MiniGoParser.LP, 0)

        def RP(self):
            return self.getToken(MiniGoParser.RP, 0)

        def stmtend(self):
            return self.getTypedRuleContext(MiniGoParser.StmtendContext,0)


        def para_declare(self):
            return self.getTypedRuleContext(MiniGoParser.Para_declareContext,0)


        def types_specifier(self):
            return self.getTypedRuleContext(MiniGoParser.Types_specifierContext,0)


        def interface_method(self):
            return self.getTypedRuleContext(MiniGoParser.Interface_methodContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_interface_method

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInterface_method" ):
                return visitor.visitInterface_method(self)
            else:
                return visitor.visitChildren(self)




    def interface_method(self):

        localctx = MiniGoParser.Interface_methodContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_interface_method)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 264
            self.match(MiniGoParser.ID)
            self.state = 265
            self.match(MiniGoParser.LP)
            self.state = 267
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.ID:
                self.state = 266
                self.para_declare()


            self.state = 269
            self.match(MiniGoParser.RP)
            self.state = 271
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.LSB) | (1 << MiniGoParser.ID))) != 0):
                self.state = 270
                self.types_specifier()


            self.state = 273
            self.stmtend()
            self.state = 275
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.ID:
                self.state = 274
                self.interface_method()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_declaredContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(MiniGoParser.FUNC, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def LP(self):
            return self.getToken(MiniGoParser.LP, 0)

        def RP(self):
            return self.getToken(MiniGoParser.RP, 0)

        def block_statement(self):
            return self.getTypedRuleContext(MiniGoParser.Block_statementContext,0)


        def para_declare(self):
            return self.getTypedRuleContext(MiniGoParser.Para_declareContext,0)


        def types_specifier(self):
            return self.getTypedRuleContext(MiniGoParser.Types_specifierContext,0)


        def ignore(self):
            return self.getTypedRuleContext(MiniGoParser.IgnoreContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_function_declared

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_declared" ):
                return visitor.visitFunction_declared(self)
            else:
                return visitor.visitChildren(self)




    def function_declared(self):

        localctx = MiniGoParser.Function_declaredContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_function_declared)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 277
            self.match(MiniGoParser.FUNC)
            self.state = 278
            self.match(MiniGoParser.ID)
            self.state = 279
            self.match(MiniGoParser.LP)
            self.state = 281
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.ID:
                self.state = 280
                self.para_declare()


            self.state = 283
            self.match(MiniGoParser.RP)
            self.state = 285
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.LSB) | (1 << MiniGoParser.ID))) != 0):
                self.state = 284
                self.types_specifier()


            self.state = 288
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.NEWLINE:
                self.state = 287
                self.ignore()


            self.state = 290
            self.block_statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Para_declareContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def list_identifiers(self):
            return self.getTypedRuleContext(MiniGoParser.List_identifiersContext,0)


        def types_specifier(self):
            return self.getTypedRuleContext(MiniGoParser.Types_specifierContext,0)


        def CM(self):
            return self.getToken(MiniGoParser.CM, 0)

        def para_declare(self):
            return self.getTypedRuleContext(MiniGoParser.Para_declareContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_para_declare

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPara_declare" ):
                return visitor.visitPara_declare(self)
            else:
                return visitor.visitChildren(self)




    def para_declare(self):

        localctx = MiniGoParser.Para_declareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_para_declare)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 292
            self.list_identifiers()
            self.state = 293
            self.types_specifier()
            self.state = 296
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.CM:
                self.state = 294
                self.match(MiniGoParser.CM)
                self.state = 295
                self.para_declare()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Para_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression6(self):
            return self.getTypedRuleContext(MiniGoParser.Expression6Context,0)


        def types_specifier(self):
            return self.getTypedRuleContext(MiniGoParser.Types_specifierContext,0)


        def CM(self):
            return self.getToken(MiniGoParser.CM, 0)

        def para_list(self):
            return self.getTypedRuleContext(MiniGoParser.Para_listContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_para_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPara_list" ):
                return visitor.visitPara_list(self)
            else:
                return visitor.visitChildren(self)




    def para_list(self):

        localctx = MiniGoParser.Para_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_para_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 298
            self.expression6(0)
            self.state = 300
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.LSB) | (1 << MiniGoParser.ID))) != 0):
                self.state = 299
                self.types_specifier()


            self.state = 304
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.CM:
                self.state = 302
                self.match(MiniGoParser.CM)
                self.state = 303
                self.para_list()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_declaredContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(MiniGoParser.FUNC, 0)

        def LP(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.LP)
            else:
                return self.getToken(MiniGoParser.LP, i)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.ID)
            else:
                return self.getToken(MiniGoParser.ID, i)

        def RP(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.RP)
            else:
                return self.getToken(MiniGoParser.RP, i)

        def block_statement(self):
            return self.getTypedRuleContext(MiniGoParser.Block_statementContext,0)


        def para_declare(self):
            return self.getTypedRuleContext(MiniGoParser.Para_declareContext,0)


        def types_specifier(self):
            return self.getTypedRuleContext(MiniGoParser.Types_specifierContext,0)


        def ignore(self):
            return self.getTypedRuleContext(MiniGoParser.IgnoreContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_method_declared

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod_declared" ):
                return visitor.visitMethod_declared(self)
            else:
                return visitor.visitChildren(self)




    def method_declared(self):

        localctx = MiniGoParser.Method_declaredContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_method_declared)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 306
            self.match(MiniGoParser.FUNC)
            self.state = 307
            self.match(MiniGoParser.LP)
            self.state = 308
            self.match(MiniGoParser.ID)
            self.state = 309
            self.match(MiniGoParser.ID)
            self.state = 310
            self.match(MiniGoParser.RP)
            self.state = 311
            self.match(MiniGoParser.ID)
            self.state = 312
            self.match(MiniGoParser.LP)
            self.state = 314
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.ID:
                self.state = 313
                self.para_declare()


            self.state = 316
            self.match(MiniGoParser.RP)
            self.state = 318
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.LSB) | (1 << MiniGoParser.ID))) != 0):
                self.state = 317
                self.types_specifier()


            self.state = 321
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.NEWLINE:
                self.state = 320
                self.ignore()


            self.state = 323
            self.block_statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_identifiersContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def CM(self):
            return self.getToken(MiniGoParser.CM, 0)

        def list_identifiers(self):
            return self.getTypedRuleContext(MiniGoParser.List_identifiersContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_list_identifiers

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_identifiers" ):
                return visitor.visitList_identifiers(self)
            else:
                return visitor.visitChildren(self)




    def list_identifiers(self):

        localctx = MiniGoParser.List_identifiersContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_list_identifiers)
        try:
            self.state = 329
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 325
                self.match(MiniGoParser.ID)
                self.state = 326
                self.match(MiniGoParser.CM)
                self.state = 327
                self.list_identifiers()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 328
                self.match(MiniGoParser.ID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Types_specifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def basic_type(self):
            return self.getTypedRuleContext(MiniGoParser.Basic_typeContext,0)


        def array_type(self):
            return self.getTypedRuleContext(MiniGoParser.Array_typeContext,0)


        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_types_specifier

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypes_specifier" ):
                return visitor.visitTypes_specifier(self)
            else:
                return visitor.visitChildren(self)




    def types_specifier(self):

        localctx = MiniGoParser.Types_specifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_types_specifier)
        try:
            self.state = 334
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.STRING, MiniGoParser.INT, MiniGoParser.FLOAT, MiniGoParser.BOOLEAN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 331
                self.basic_type()
                pass
            elif token in [MiniGoParser.LSB]:
                self.enterOuterAlt(localctx, 2)
                self.state = 332
                self.array_type()
                pass
            elif token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 3)
                self.state = 333
                self.match(MiniGoParser.ID)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Basic_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(MiniGoParser.INT, 0)

        def BOOLEAN(self):
            return self.getToken(MiniGoParser.BOOLEAN, 0)

        def FLOAT(self):
            return self.getToken(MiniGoParser.FLOAT, 0)

        def STRING(self):
            return self.getToken(MiniGoParser.STRING, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_basic_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBasic_type" ):
                return visitor.visitBasic_type(self)
            else:
                return visitor.visitChildren(self)




    def basic_type(self):

        localctx = MiniGoParser.Basic_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_basic_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 336
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self):
            return self.getTypedRuleContext(MiniGoParser.StatementContext,0)


        def list_statement(self):
            return self.getTypedRuleContext(MiniGoParser.List_statementContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_list_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_statement" ):
                return visitor.visitList_statement(self)
            else:
                return visitor.visitChildren(self)




    def list_statement(self):

        localctx = MiniGoParser.List_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_list_statement)
        try:
            self.state = 342
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 338
                self.statement()
                self.state = 339
                self.list_statement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 341
                self.statement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmtend(self):
            return self.getTypedRuleContext(MiniGoParser.StmtendContext,0)


        def declared_statement(self):
            return self.getTypedRuleContext(MiniGoParser.Declared_statementContext,0)


        def assign_statement(self):
            return self.getTypedRuleContext(MiniGoParser.Assign_statementContext,0)


        def if_statement(self):
            return self.getTypedRuleContext(MiniGoParser.If_statementContext,0)


        def for_statement(self):
            return self.getTypedRuleContext(MiniGoParser.For_statementContext,0)


        def break_statement(self):
            return self.getTypedRuleContext(MiniGoParser.Break_statementContext,0)


        def continue_statement(self):
            return self.getTypedRuleContext(MiniGoParser.Continue_statementContext,0)


        def call_statement(self):
            return self.getTypedRuleContext(MiniGoParser.Call_statementContext,0)


        def return_statement(self):
            return self.getTypedRuleContext(MiniGoParser.Return_statementContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = MiniGoParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 352
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                self.state = 344
                self.declared_statement()
                pass

            elif la_ == 2:
                self.state = 345
                self.assign_statement()
                pass

            elif la_ == 3:
                self.state = 346
                self.if_statement()
                pass

            elif la_ == 4:
                self.state = 347
                self.for_statement()
                pass

            elif la_ == 5:
                self.state = 348
                self.break_statement()
                pass

            elif la_ == 6:
                self.state = 349
                self.continue_statement()
                pass

            elif la_ == 7:
                self.state = 350
                self.call_statement()
                pass

            elif la_ == 8:
                self.state = 351
                self.return_statement()
                pass


            self.state = 354
            self.stmtend()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assign_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def nolit(self):
            return self.getTypedRuleContext(MiniGoParser.NolitContext,0)


        def assign(self):
            return self.getTypedRuleContext(MiniGoParser.AssignContext,0)


        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_assign_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign_statement" ):
                return visitor.visitAssign_statement(self)
            else:
                return visitor.visitChildren(self)




    def assign_statement(self):

        localctx = MiniGoParser.Assign_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_assign_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 356
            self.nolit(0)
            self.state = 357
            self.assign()
            self.state = 358
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(MiniGoParser.RETURN, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_return_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_statement" ):
                return visitor.visitReturn_statement(self)
            else:
                return visitor.visitChildren(self)




    def return_statement(self):

        localctx = MiniGoParser.Return_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_return_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 360
            self.match(MiniGoParser.RETURN)
            self.state = 362
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.NIL) | (1 << MiniGoParser.TRUE) | (1 << MiniGoParser.FALSE) | (1 << MiniGoParser.SUB) | (1 << MiniGoParser.NOT) | (1 << MiniGoParser.LSB) | (1 << MiniGoParser.LP) | (1 << MiniGoParser.INT_LIT) | (1 << MiniGoParser.FLOAT_LIT) | (1 << MiniGoParser.HEX_LIT) | (1 << MiniGoParser.BI_LIT) | (1 << MiniGoParser.OCT_LIT) | (1 << MiniGoParser.ID) | (1 << MiniGoParser.STRING_LIT))) != 0):
                self.state = 361
                self.expression(0)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Block_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LCB(self):
            return self.getToken(MiniGoParser.LCB, 0)

        def RCB(self):
            return self.getToken(MiniGoParser.RCB, 0)

        def stmtend(self):
            return self.getTypedRuleContext(MiniGoParser.StmtendContext,0)


        def list_statement(self):
            return self.getTypedRuleContext(MiniGoParser.List_statementContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_block_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock_statement" ):
                return visitor.visitBlock_statement(self)
            else:
                return visitor.visitChildren(self)




    def block_statement(self):

        localctx = MiniGoParser.Block_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_block_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 364
            self.match(MiniGoParser.LCB)
            self.state = 366
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.SC or _la==MiniGoParser.NEWLINE:
                self.state = 365
                self.stmtend()


            self.state = 369
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.IF) | (1 << MiniGoParser.FOR) | (1 << MiniGoParser.RETURN) | (1 << MiniGoParser.FUNC) | (1 << MiniGoParser.TYPE) | (1 << MiniGoParser.CONST) | (1 << MiniGoParser.VAR) | (1 << MiniGoParser.CONTINUE) | (1 << MiniGoParser.BREAK) | (1 << MiniGoParser.NIL) | (1 << MiniGoParser.TRUE) | (1 << MiniGoParser.FALSE) | (1 << MiniGoParser.LSB) | (1 << MiniGoParser.LP) | (1 << MiniGoParser.INT_LIT) | (1 << MiniGoParser.FLOAT_LIT) | (1 << MiniGoParser.HEX_LIT) | (1 << MiniGoParser.BI_LIT) | (1 << MiniGoParser.OCT_LIT) | (1 << MiniGoParser.ID) | (1 << MiniGoParser.STRING_LIT))) != 0):
                self.state = 368
                self.list_statement()


            self.state = 371
            self.match(MiniGoParser.RCB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(MiniGoParser.IF, 0)

        def LP(self):
            return self.getToken(MiniGoParser.LP, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def RP(self):
            return self.getToken(MiniGoParser.RP, 0)

        def block_statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.Block_statementContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.Block_statementContext,i)


        def else_if(self):
            return self.getTypedRuleContext(MiniGoParser.Else_ifContext,0)


        def ignore(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.IgnoreContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.IgnoreContext,i)


        def ELSE(self):
            return self.getToken(MiniGoParser.ELSE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_if_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_statement" ):
                return visitor.visitIf_statement(self)
            else:
                return visitor.visitChildren(self)




    def if_statement(self):

        localctx = MiniGoParser.If_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_if_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 373
            self.match(MiniGoParser.IF)
            self.state = 374
            self.match(MiniGoParser.LP)
            self.state = 375
            self.expression(0)
            self.state = 376
            self.match(MiniGoParser.RP)
            self.state = 378
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.NEWLINE:
                self.state = 377
                self.ignore()


            self.state = 380
            self.block_statement()
            self.state = 381
            self.else_if()
            self.state = 387
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.ELSE:
                self.state = 382
                self.match(MiniGoParser.ELSE)
                self.state = 384
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==MiniGoParser.NEWLINE:
                    self.state = 383
                    self.ignore()


                self.state = 386
                self.block_statement()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Else_ifContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(MiniGoParser.ELSE, 0)

        def IF(self):
            return self.getToken(MiniGoParser.IF, 0)

        def LP(self):
            return self.getToken(MiniGoParser.LP, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def RP(self):
            return self.getToken(MiniGoParser.RP, 0)

        def block_statement(self):
            return self.getTypedRuleContext(MiniGoParser.Block_statementContext,0)


        def else_if(self):
            return self.getTypedRuleContext(MiniGoParser.Else_ifContext,0)


        def ignore(self):
            return self.getTypedRuleContext(MiniGoParser.IgnoreContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_else_if

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElse_if" ):
                return visitor.visitElse_if(self)
            else:
                return visitor.visitChildren(self)




    def else_if(self):

        localctx = MiniGoParser.Else_ifContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_else_if)
        self._la = 0 # Token type
        try:
            self.state = 401
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,44,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 389
                self.match(MiniGoParser.ELSE)
                self.state = 390
                self.match(MiniGoParser.IF)
                self.state = 391
                self.match(MiniGoParser.LP)
                self.state = 392
                self.expression(0)
                self.state = 393
                self.match(MiniGoParser.RP)
                self.state = 395
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==MiniGoParser.NEWLINE:
                    self.state = 394
                    self.ignore()


                self.state = 397
                self.block_statement()
                self.state = 398
                self.else_if()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def range_for(self):
            return self.getTypedRuleContext(MiniGoParser.Range_forContext,0)


        def index_for(self):
            return self.getTypedRuleContext(MiniGoParser.Index_forContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_for_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_statement" ):
                return visitor.visitFor_statement(self)
            else:
                return visitor.visitChildren(self)




    def for_statement(self):

        localctx = MiniGoParser.For_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_for_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 405
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,45,self._ctx)
            if la_ == 1:
                self.state = 403
                self.range_for()
                pass

            elif la_ == 2:
                self.state = 404
                self.index_for()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Range_forContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(MiniGoParser.FOR, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.ID)
            else:
                return self.getToken(MiniGoParser.ID, i)

        def CM(self):
            return self.getToken(MiniGoParser.CM, 0)

        def ASSIGN(self):
            return self.getToken(MiniGoParser.ASSIGN, 0)

        def RANGE(self):
            return self.getToken(MiniGoParser.RANGE, 0)

        def expression6(self):
            return self.getTypedRuleContext(MiniGoParser.Expression6Context,0)


        def block_statement(self):
            return self.getTypedRuleContext(MiniGoParser.Block_statementContext,0)


        def ignore(self):
            return self.getTypedRuleContext(MiniGoParser.IgnoreContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_range_for

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRange_for" ):
                return visitor.visitRange_for(self)
            else:
                return visitor.visitChildren(self)




    def range_for(self):

        localctx = MiniGoParser.Range_forContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_range_for)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 407
            self.match(MiniGoParser.FOR)
            self.state = 408
            self.match(MiniGoParser.ID)
            self.state = 409
            self.match(MiniGoParser.CM)
            self.state = 410
            self.match(MiniGoParser.ID)
            self.state = 411
            self.match(MiniGoParser.ASSIGN)
            self.state = 412
            self.match(MiniGoParser.RANGE)
            self.state = 413
            self.expression6(0)
            self.state = 415
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.NEWLINE:
                self.state = 414
                self.ignore()


            self.state = 417
            self.block_statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Index_forContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(MiniGoParser.FOR, 0)

        def block_statement(self):
            return self.getTypedRuleContext(MiniGoParser.Block_statementContext,0)


        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.ExpressionContext,i)


        def stmtend(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.StmtendContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.StmtendContext,i)


        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.ID)
            else:
                return self.getToken(MiniGoParser.ID, i)

        def assign(self):
            return self.getTypedRuleContext(MiniGoParser.AssignContext,0)


        def assign_statement(self):
            return self.getTypedRuleContext(MiniGoParser.Assign_statementContext,0)


        def VAR(self):
            return self.getToken(MiniGoParser.VAR, 0)

        def ASSIGNINIT(self):
            return self.getToken(MiniGoParser.ASSIGNINIT, 0)

        def types_specifier(self):
            return self.getTypedRuleContext(MiniGoParser.Types_specifierContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_index_for

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndex_for" ):
                return visitor.visitIndex_for(self)
            else:
                return visitor.visitChildren(self)




    def index_for(self):

        localctx = MiniGoParser.Index_forContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_index_for)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 419
            self.match(MiniGoParser.FOR)
            self.state = 438
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,49,self._ctx)
            if la_ == 1:
                self.state = 420
                self.expression(0)
                pass

            elif la_ == 2:
                self.state = 429
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [MiniGoParser.ID]:
                    self.state = 421
                    self.assign_statement()
                    pass
                elif token in [MiniGoParser.VAR]:
                    self.state = 422
                    self.match(MiniGoParser.VAR)
                    self.state = 423
                    self.match(MiniGoParser.ID)
                    self.state = 425
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.LSB) | (1 << MiniGoParser.ID))) != 0):
                        self.state = 424
                        self.types_specifier()


                    self.state = 427
                    self.match(MiniGoParser.ASSIGNINIT)
                    self.state = 428
                    self.expression(0)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 431
                self.stmtend()
                self.state = 432
                self.expression(0)
                self.state = 433
                self.stmtend()
                self.state = 434
                self.match(MiniGoParser.ID)
                self.state = 435
                self.assign()
                self.state = 436
                self.expression(0)
                pass


            self.state = 440
            self.block_statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Break_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(MiniGoParser.BREAK, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_break_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreak_statement" ):
                return visitor.visitBreak_statement(self)
            else:
                return visitor.visitChildren(self)




    def break_statement(self):

        localctx = MiniGoParser.Break_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_break_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 442
            self.match(MiniGoParser.BREAK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Continue_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(MiniGoParser.CONTINUE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_continue_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinue_statement" ):
                return visitor.visitContinue_statement(self)
            else:
                return visitor.visitChildren(self)




    def continue_statement(self):

        localctx = MiniGoParser.Continue_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_continue_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 444
            self.match(MiniGoParser.CONTINUE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Call_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression6(self):
            return self.getTypedRuleContext(MiniGoParser.Expression6Context,0)


        def LP(self):
            return self.getToken(MiniGoParser.LP, 0)

        def RP(self):
            return self.getToken(MiniGoParser.RP, 0)

        def list_expression(self):
            return self.getTypedRuleContext(MiniGoParser.List_expressionContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_call_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCall_statement" ):
                return visitor.visitCall_statement(self)
            else:
                return visitor.visitChildren(self)




    def call_statement(self):

        localctx = MiniGoParser.Call_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_call_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 446
            self.expression6(0)
            self.state = 447
            self.match(MiniGoParser.LP)
            self.state = 449
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.NIL) | (1 << MiniGoParser.TRUE) | (1 << MiniGoParser.FALSE) | (1 << MiniGoParser.SUB) | (1 << MiniGoParser.NOT) | (1 << MiniGoParser.LSB) | (1 << MiniGoParser.LP) | (1 << MiniGoParser.INT_LIT) | (1 << MiniGoParser.FLOAT_LIT) | (1 << MiniGoParser.HEX_LIT) | (1 << MiniGoParser.BI_LIT) | (1 << MiniGoParser.OCT_LIT) | (1 << MiniGoParser.ID) | (1 << MiniGoParser.STRING_LIT))) != 0):
                self.state = 448
                self.list_expression()


            self.state = 451
            self.match(MiniGoParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def CM(self):
            return self.getToken(MiniGoParser.CM, 0)

        def list_expression(self):
            return self.getTypedRuleContext(MiniGoParser.List_expressionContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_list_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_expression" ):
                return visitor.visitList_expression(self)
            else:
                return visitor.visitChildren(self)




    def list_expression(self):

        localctx = MiniGoParser.List_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_list_expression)
        try:
            self.state = 458
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,51,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 453
                self.expression(0)
                self.state = 454
                self.match(MiniGoParser.CM)
                self.state = 455
                self.list_expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 457
                self.expression(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression1(self):
            return self.getTypedRuleContext(MiniGoParser.Expression1Context,0)


        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def OR(self):
            return self.getToken(MiniGoParser.OR, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 86
        self.enterRecursionRule(localctx, 86, self.RULE_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 461
            self.expression1(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 468
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,52,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.ExpressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                    self.state = 463
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 464
                    self.match(MiniGoParser.OR)
                    self.state = 465
                    self.expression1(0) 
                self.state = 470
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,52,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expression1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression2(self):
            return self.getTypedRuleContext(MiniGoParser.Expression2Context,0)


        def expression1(self):
            return self.getTypedRuleContext(MiniGoParser.Expression1Context,0)


        def AND(self):
            return self.getToken(MiniGoParser.AND, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expression1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression1" ):
                return visitor.visitExpression1(self)
            else:
                return visitor.visitChildren(self)



    def expression1(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expression1Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 88
        self.enterRecursionRule(localctx, 88, self.RULE_expression1, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 472
            self.expression2(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 479
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,53,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expression1Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression1)
                    self.state = 474
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 475
                    self.match(MiniGoParser.AND)
                    self.state = 476
                    self.expression2(0) 
                self.state = 481
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,53,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expression2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression3(self):
            return self.getTypedRuleContext(MiniGoParser.Expression3Context,0)


        def expression2(self):
            return self.getTypedRuleContext(MiniGoParser.Expression2Context,0)


        def EQ(self):
            return self.getToken(MiniGoParser.EQ, 0)

        def NEQ(self):
            return self.getToken(MiniGoParser.NEQ, 0)

        def LT(self):
            return self.getToken(MiniGoParser.LT, 0)

        def LTE(self):
            return self.getToken(MiniGoParser.LTE, 0)

        def GT(self):
            return self.getToken(MiniGoParser.GT, 0)

        def GTE(self):
            return self.getToken(MiniGoParser.GTE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expression2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression2" ):
                return visitor.visitExpression2(self)
            else:
                return visitor.visitChildren(self)



    def expression2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expression2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 90
        self.enterRecursionRule(localctx, 90, self.RULE_expression2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 483
            self.expression3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 490
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,54,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expression2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression2)
                    self.state = 485
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 486
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.EQ) | (1 << MiniGoParser.NEQ) | (1 << MiniGoParser.LT) | (1 << MiniGoParser.GT) | (1 << MiniGoParser.LTE) | (1 << MiniGoParser.GTE))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 487
                    self.expression3(0) 
                self.state = 492
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,54,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expression3Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression4(self):
            return self.getTypedRuleContext(MiniGoParser.Expression4Context,0)


        def expression3(self):
            return self.getTypedRuleContext(MiniGoParser.Expression3Context,0)


        def ADD(self):
            return self.getToken(MiniGoParser.ADD, 0)

        def SUB(self):
            return self.getToken(MiniGoParser.SUB, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expression3

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression3" ):
                return visitor.visitExpression3(self)
            else:
                return visitor.visitChildren(self)



    def expression3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expression3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 92
        self.enterRecursionRule(localctx, 92, self.RULE_expression3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 494
            self.expression4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 501
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,55,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expression3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression3)
                    self.state = 496
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 497
                    _la = self._input.LA(1)
                    if not(_la==MiniGoParser.ADD or _la==MiniGoParser.SUB):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 498
                    self.expression4(0) 
                self.state = 503
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,55,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expression4Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression5(self):
            return self.getTypedRuleContext(MiniGoParser.Expression5Context,0)


        def expression4(self):
            return self.getTypedRuleContext(MiniGoParser.Expression4Context,0)


        def MUL(self):
            return self.getToken(MiniGoParser.MUL, 0)

        def DIV(self):
            return self.getToken(MiniGoParser.DIV, 0)

        def MOD(self):
            return self.getToken(MiniGoParser.MOD, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expression4

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression4" ):
                return visitor.visitExpression4(self)
            else:
                return visitor.visitChildren(self)



    def expression4(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expression4Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 94
        self.enterRecursionRule(localctx, 94, self.RULE_expression4, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 505
            self.expression5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 512
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,56,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expression4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression4)
                    self.state = 507
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 508
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.MUL) | (1 << MiniGoParser.DIV) | (1 << MiniGoParser.MOD))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 509
                    self.expression5() 
                self.state = 514
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,56,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expression5Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression5(self):
            return self.getTypedRuleContext(MiniGoParser.Expression5Context,0)


        def NOT(self):
            return self.getToken(MiniGoParser.NOT, 0)

        def SUB(self):
            return self.getToken(MiniGoParser.SUB, 0)

        def expression6(self):
            return self.getTypedRuleContext(MiniGoParser.Expression6Context,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_expression5

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression5" ):
                return visitor.visitExpression5(self)
            else:
                return visitor.visitChildren(self)




    def expression5(self):

        localctx = MiniGoParser.Expression5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_expression5)
        self._la = 0 # Token type
        try:
            self.state = 518
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.SUB, MiniGoParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 515
                _la = self._input.LA(1)
                if not(_la==MiniGoParser.SUB or _la==MiniGoParser.NOT):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 516
                self.expression5()
                pass
            elif token in [MiniGoParser.NIL, MiniGoParser.TRUE, MiniGoParser.FALSE, MiniGoParser.LSB, MiniGoParser.LP, MiniGoParser.INT_LIT, MiniGoParser.FLOAT_LIT, MiniGoParser.HEX_LIT, MiniGoParser.BI_LIT, MiniGoParser.OCT_LIT, MiniGoParser.ID, MiniGoParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 517
                self.expression6(0)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expression6Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression7(self):
            return self.getTypedRuleContext(MiniGoParser.Expression7Context,0)


        def expression6(self):
            return self.getTypedRuleContext(MiniGoParser.Expression6Context,0)


        def LCB(self):
            return self.getToken(MiniGoParser.LCB, 0)

        def RCB(self):
            return self.getToken(MiniGoParser.RCB, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def DOT(self):
            return self.getToken(MiniGoParser.DOT, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def funtion_call(self):
            return self.getTypedRuleContext(MiniGoParser.Funtion_callContext,0)


        def array_dimension(self):
            return self.getTypedRuleContext(MiniGoParser.Array_dimensionContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_expression6

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression6" ):
                return visitor.visitExpression6(self)
            else:
                return visitor.visitChildren(self)



    def expression6(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expression6Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 98
        self.enterRecursionRule(localctx, 98, self.RULE_expression6, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 521
            self.expression7()
            self._ctx.stop = self._input.LT(-1)
            self.state = 539
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,60,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 537
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,59,self._ctx)
                    if la_ == 1:
                        localctx = MiniGoParser.Expression6Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression6)
                        self.state = 523
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 524
                        self.match(MiniGoParser.LCB)
                        self.state = 526
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.NIL) | (1 << MiniGoParser.TRUE) | (1 << MiniGoParser.FALSE) | (1 << MiniGoParser.SUB) | (1 << MiniGoParser.NOT) | (1 << MiniGoParser.LSB) | (1 << MiniGoParser.LP) | (1 << MiniGoParser.INT_LIT) | (1 << MiniGoParser.FLOAT_LIT) | (1 << MiniGoParser.HEX_LIT) | (1 << MiniGoParser.BI_LIT) | (1 << MiniGoParser.OCT_LIT) | (1 << MiniGoParser.ID) | (1 << MiniGoParser.STRING_LIT))) != 0):
                            self.state = 525
                            self.expression(0)


                        self.state = 528
                        self.match(MiniGoParser.RCB)
                        pass

                    elif la_ == 2:
                        localctx = MiniGoParser.Expression6Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression6)
                        self.state = 529
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 530
                        self.match(MiniGoParser.DOT)
                        self.state = 531
                        self.match(MiniGoParser.ID)
                        pass

                    elif la_ == 3:
                        localctx = MiniGoParser.Expression6Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression6)
                        self.state = 532
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 533
                        self.match(MiniGoParser.DOT)
                        self.state = 534
                        self.funtion_call()
                        pass

                    elif la_ == 4:
                        localctx = MiniGoParser.Expression6Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression6)
                        self.state = 535
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 536
                        self.array_dimension()
                        pass

             
                self.state = 541
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,60,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expression7Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def literal(self):
            return self.getTypedRuleContext(MiniGoParser.LiteralContext,0)


        def funtion_call(self):
            return self.getTypedRuleContext(MiniGoParser.Funtion_callContext,0)


        def LP(self):
            return self.getToken(MiniGoParser.LP, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def RP(self):
            return self.getToken(MiniGoParser.RP, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expression7

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression7" ):
                return visitor.visitExpression7(self)
            else:
                return visitor.visitChildren(self)




    def expression7(self):

        localctx = MiniGoParser.Expression7Context(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_expression7)
        try:
            self.state = 549
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,61,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 542
                self.match(MiniGoParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 543
                self.literal()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 544
                self.funtion_call()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 545
                self.match(MiniGoParser.LP)
                self.state = 546
                self.expression(0)
                self.state = 547
                self.match(MiniGoParser.RP)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Funtion_callContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def LP(self):
            return self.getToken(MiniGoParser.LP, 0)

        def RP(self):
            return self.getToken(MiniGoParser.RP, 0)

        def list_expression(self):
            return self.getTypedRuleContext(MiniGoParser.List_expressionContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_funtion_call

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuntion_call" ):
                return visitor.visitFuntion_call(self)
            else:
                return visitor.visitChildren(self)




    def funtion_call(self):

        localctx = MiniGoParser.Funtion_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_funtion_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 551
            self.match(MiniGoParser.ID)
            self.state = 552
            self.match(MiniGoParser.LP)
            self.state = 554
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.NIL) | (1 << MiniGoParser.TRUE) | (1 << MiniGoParser.FALSE) | (1 << MiniGoParser.SUB) | (1 << MiniGoParser.NOT) | (1 << MiniGoParser.LSB) | (1 << MiniGoParser.LP) | (1 << MiniGoParser.INT_LIT) | (1 << MiniGoParser.FLOAT_LIT) | (1 << MiniGoParser.HEX_LIT) | (1 << MiniGoParser.BI_LIT) | (1 << MiniGoParser.OCT_LIT) | (1 << MiniGoParser.ID) | (1 << MiniGoParser.STRING_LIT))) != 0):
                self.state = 553
                self.list_expression()


            self.state = 556
            self.match(MiniGoParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_checkContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def funtion_call(self):
            return self.getTypedRuleContext(MiniGoParser.Funtion_callContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_var_check

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_check" ):
                return visitor.visitVar_check(self)
            else:
                return visitor.visitChildren(self)




    def var_check(self):

        localctx = MiniGoParser.Var_checkContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_var_check)
        try:
            self.state = 560
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,63,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 558
                self.match(MiniGoParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 559
                self.funtion_call()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NolitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_check(self):
            return self.getTypedRuleContext(MiniGoParser.Var_checkContext,0)


        def nolit(self):
            return self.getTypedRuleContext(MiniGoParser.NolitContext,0)


        def DOT(self):
            return self.getToken(MiniGoParser.DOT, 0)

        def array_dimension(self):
            return self.getTypedRuleContext(MiniGoParser.Array_dimensionContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_nolit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNolit" ):
                return visitor.visitNolit(self)
            else:
                return visitor.visitChildren(self)



    def nolit(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.NolitContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 106
        self.enterRecursionRule(localctx, 106, self.RULE_nolit, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 563
            self.var_check()
            self._ctx.stop = self._input.LT(-1)
            self.state = 572
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,65,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 570
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,64,self._ctx)
                    if la_ == 1:
                        localctx = MiniGoParser.NolitContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_nolit)
                        self.state = 565
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 566
                        self.match(MiniGoParser.DOT)
                        self.state = 567
                        self.var_check()
                        pass

                    elif la_ == 2:
                        localctx = MiniGoParser.NolitContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_nolit)
                        self.state = 568
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 569
                        self.array_dimension()
                        pass

             
                self.state = 574
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,65,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class AssignContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ASSIGN(self):
            return self.getToken(MiniGoParser.ASSIGN, 0)

        def E_DIV(self):
            return self.getToken(MiniGoParser.E_DIV, 0)

        def E_MOD(self):
            return self.getToken(MiniGoParser.E_MOD, 0)

        def E_ADD(self):
            return self.getToken(MiniGoParser.E_ADD, 0)

        def E_SUB(self):
            return self.getToken(MiniGoParser.E_SUB, 0)

        def E_MUL(self):
            return self.getToken(MiniGoParser.E_MUL, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_assign

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign" ):
                return visitor.visitAssign(self)
            else:
                return visitor.visitChildren(self)




    def assign(self):

        localctx = MiniGoParser.AssignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_assign)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 575
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.ASSIGN) | (1 << MiniGoParser.E_DIV) | (1 << MiniGoParser.E_MOD) | (1 << MiniGoParser.E_ADD) | (1 << MiniGoParser.E_SUB) | (1 << MiniGoParser.E_MUL))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtendContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEWLINE(self):
            return self.getToken(MiniGoParser.NEWLINE, 0)

        def SC(self):
            return self.getToken(MiniGoParser.SC, 0)

        def stmtend(self):
            return self.getTypedRuleContext(MiniGoParser.StmtendContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_stmtend

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmtend" ):
                return visitor.visitStmtend(self)
            else:
                return visitor.visitChildren(self)




    def stmtend(self):

        localctx = MiniGoParser.StmtendContext(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_stmtend)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 577
            _la = self._input.LA(1)
            if not(_la==MiniGoParser.SC or _la==MiniGoParser.NEWLINE):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 579
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,66,self._ctx)
            if la_ == 1:
                self.state = 578
                self.stmtend()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IgnoreContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEWLINE(self):
            return self.getToken(MiniGoParser.NEWLINE, 0)

        def ignore(self):
            return self.getTypedRuleContext(MiniGoParser.IgnoreContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_ignore

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIgnore" ):
                return visitor.visitIgnore(self)
            else:
                return visitor.visitChildren(self)




    def ignore(self):

        localctx = MiniGoParser.IgnoreContext(self, self._ctx, self.state)
        self.enterRule(localctx, 112, self.RULE_ignore)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 581
            self.match(MiniGoParser.NEWLINE)
            self.state = 583
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.NEWLINE:
                self.state = 582
                self.ignore()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[43] = self.expression_sempred
        self._predicates[44] = self.expression1_sempred
        self._predicates[45] = self.expression2_sempred
        self._predicates[46] = self.expression3_sempred
        self._predicates[47] = self.expression4_sempred
        self._predicates[49] = self.expression6_sempred
        self._predicates[53] = self.nolit_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def expression1_sempred(self, localctx:Expression1Context, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def expression2_sempred(self, localctx:Expression2Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def expression3_sempred(self, localctx:Expression3Context, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         

    def expression4_sempred(self, localctx:Expression4Context, predIndex:int):
            if predIndex == 4:
                return self.precpred(self._ctx, 2)
         

    def expression6_sempred(self, localctx:Expression6Context, predIndex:int):
            if predIndex == 5:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 7:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 8:
                return self.precpred(self._ctx, 2)
         

    def nolit_sempred(self, localctx:NolitContext, predIndex:int):
            if predIndex == 9:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 10:
                return self.precpred(self._ctx, 2)
         




