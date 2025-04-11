# Generated from main/MiniGo.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2E")
        buf.write("\u01fd\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\3\2\3\2\3\2\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5")
        buf.write("\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3")
        buf.write("\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t")
        buf.write("\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\5\n\u00c9\n\n\3\13")
        buf.write("\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3")
        buf.write("\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\16\3\17")
        buf.write("\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\21\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22")
        buf.write("\3\22\3\22\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24")
        buf.write("\3\25\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\27\3\27\3\30")
        buf.write("\3\30\3\31\3\31\3\32\3\32\3\33\3\33\3\33\3\34\3\34\3\34")
        buf.write("\3\35\3\35\3\36\3\36\3\37\3\37\3\37\3 \3 \3 \3!\3!\3\"")
        buf.write("\3\"\3\"\3#\3#\3$\3$\3$\3%\3%\3%\3&\3&\3&\3\'\3\'\3\'")
        buf.write("\3(\3(\3(\3)\3)\3)\3*\3*\3+\3+\3+\3,\3,\3,\3-\3-\3.\3")
        buf.write(".\3/\3/\3\60\3\60\3\61\3\61\3\62\3\62\3\63\3\63\3\64\3")
        buf.write("\64\3\65\3\65\3\66\3\66\3\67\3\67\3\67\7\67\u015d\n\67")
        buf.write("\f\67\16\67\u0160\13\67\5\67\u0162\n\67\38\68\u0165\n")
        buf.write("8\r8\168\u0166\38\38\78\u016b\n8\f8\168\u016e\138\38\3")
        buf.write("8\58\u0172\n8\38\68\u0175\n8\r8\168\u0176\58\u0179\n8")
        buf.write("\39\39\39\59\u017e\n9\39\69\u0181\n9\r9\169\u0182\3:\3")
        buf.write(":\3:\5:\u0188\n:\3:\6:\u018b\n:\r:\16:\u018c\3;\3;\3;")
        buf.write("\5;\u0192\n;\3;\6;\u0195\n;\r;\16;\u0196\3<\3<\5<\u019b")
        buf.write("\n<\3=\3=\7=\u019f\n=\f=\16=\u01a2\13=\3>\3>\7>\u01a6")
        buf.write("\n>\f>\16>\u01a9\13>\3>\3>\3?\3?\5?\u01af\n?\3@\3@\3@")
        buf.write("\3@\5@\u01b5\n@\3A\3A\3A\5A\u01ba\nA\3B\3B\3B\3B\7B\u01c0")
        buf.write("\nB\fB\16B\u01c3\13B\3B\3B\3C\3C\3C\3C\3C\7C\u01cc\nC")
        buf.write("\fC\16C\u01cf\13C\3C\3C\3C\3C\3C\3D\5D\u01d7\nD\3D\3D")
        buf.write("\3D\3E\6E\u01dd\nE\rE\16E\u01de\3E\3E\3F\3F\3F\3G\3G\3")
        buf.write("G\3G\7G\u01ea\nG\fG\16G\u01ed\13G\3G\5G\u01f0\nG\3G\3")
        buf.write("G\3H\3H\7H\u01f6\nH\fH\16H\u01f9\13H\3H\3H\3H\3\u01cd")
        buf.write("\2I\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r")
        buf.write("\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30")
        buf.write("/\31\61\32\63\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'")
        buf.write("M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63e\64g\65i\66k\67m\2o8")
        buf.write("q9s:u;w<y={>}\2\177\2\u0081\2\u0083?\u0085@\u0087A\u0089")
        buf.write("B\u008bC\u008dD\u008fE\3\2\27\3\2\63;\3\2\62;\4\2GGgg")
        buf.write("\4\2--//\4\2ZZzz\5\2\62;CHch\4\2DDdd\3\2\62\63\4\2QQq")
        buf.write("q\3\2\629\5\2C\\aac|\6\2\62;C\\aac|\6\2\f\f\17\17$$^^")
        buf.write("\6\2^^ppttvv\3\2\17\17\7\2))^^ppttvv\3\2\f\f\5\2\n\13")
        buf.write("\16\17\"\"\5\2\f\f$$^^\t\2$$^^ddhhppttvv\3\3\f\f\2\u0214")
        buf.write("\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13")
        buf.write("\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3")
        buf.write("\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2")
        buf.write("\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2")
        buf.write("%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2")
        buf.write("\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67")
        buf.write("\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2")
        buf.write("A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2")
        buf.write("\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2")
        buf.write("\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2")
        buf.write("\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3")
        buf.write("\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s")
        buf.write("\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2")
        buf.write("\u0083\3\2\2\2\2\u0085\3\2\2\2\2\u0087\3\2\2\2\2\u0089")
        buf.write("\3\2\2\2\2\u008b\3\2\2\2\2\u008d\3\2\2\2\2\u008f\3\2\2")
        buf.write("\2\3\u0091\3\2\2\2\5\u0094\3\2\2\2\7\u0099\3\2\2\2\t\u009d")
        buf.write("\3\2\2\2\13\u00a4\3\2\2\2\r\u00a9\3\2\2\2\17\u00ae\3\2")
        buf.write("\2\2\21\u00b5\3\2\2\2\23\u00c8\3\2\2\2\25\u00ca\3\2\2")
        buf.write("\2\27\u00ce\3\2\2\2\31\u00d4\3\2\2\2\33\u00dc\3\2\2\2")
        buf.write("\35\u00e2\3\2\2\2\37\u00e6\3\2\2\2!\u00ef\3\2\2\2#\u00f5")
        buf.write("\3\2\2\2%\u00fb\3\2\2\2\'\u00ff\3\2\2\2)\u0104\3\2\2\2")
        buf.write("+\u010a\3\2\2\2-\u010c\3\2\2\2/\u010e\3\2\2\2\61\u0110")
        buf.write("\3\2\2\2\63\u0112\3\2\2\2\65\u0114\3\2\2\2\67\u0117\3")
        buf.write("\2\2\29\u011a\3\2\2\2;\u011c\3\2\2\2=\u011e\3\2\2\2?\u0121")
        buf.write("\3\2\2\2A\u0124\3\2\2\2C\u0126\3\2\2\2E\u0129\3\2\2\2")
        buf.write("G\u012b\3\2\2\2I\u012e\3\2\2\2K\u0131\3\2\2\2M\u0134\3")
        buf.write("\2\2\2O\u0137\3\2\2\2Q\u013a\3\2\2\2S\u013d\3\2\2\2U\u013f")
        buf.write("\3\2\2\2W\u0142\3\2\2\2Y\u0145\3\2\2\2[\u0147\3\2\2\2")
        buf.write("]\u0149\3\2\2\2_\u014b\3\2\2\2a\u014d\3\2\2\2c\u014f\3")
        buf.write("\2\2\2e\u0151\3\2\2\2g\u0153\3\2\2\2i\u0155\3\2\2\2k\u0157")
        buf.write("\3\2\2\2m\u0161\3\2\2\2o\u0164\3\2\2\2q\u017a\3\2\2\2")
        buf.write("s\u0184\3\2\2\2u\u018e\3\2\2\2w\u019a\3\2\2\2y\u019c\3")
        buf.write("\2\2\2{\u01a3\3\2\2\2}\u01ae\3\2\2\2\177\u01b4\3\2\2\2")
        buf.write("\u0081\u01b9\3\2\2\2\u0083\u01bb\3\2\2\2\u0085\u01c6\3")
        buf.write("\2\2\2\u0087\u01d6\3\2\2\2\u0089\u01dc\3\2\2\2\u008b\u01e2")
        buf.write("\3\2\2\2\u008d\u01e5\3\2\2\2\u008f\u01f3\3\2\2\2\u0091")
        buf.write("\u0092\7k\2\2\u0092\u0093\7h\2\2\u0093\4\3\2\2\2\u0094")
        buf.write("\u0095\7g\2\2\u0095\u0096\7n\2\2\u0096\u0097\7u\2\2\u0097")
        buf.write("\u0098\7g\2\2\u0098\6\3\2\2\2\u0099\u009a\7h\2\2\u009a")
        buf.write("\u009b\7q\2\2\u009b\u009c\7t\2\2\u009c\b\3\2\2\2\u009d")
        buf.write("\u009e\7t\2\2\u009e\u009f\7g\2\2\u009f\u00a0\7v\2\2\u00a0")
        buf.write("\u00a1\7w\2\2\u00a1\u00a2\7t\2\2\u00a2\u00a3\7p\2\2\u00a3")
        buf.write("\n\3\2\2\2\u00a4\u00a5\7h\2\2\u00a5\u00a6\7w\2\2\u00a6")
        buf.write("\u00a7\7p\2\2\u00a7\u00a8\7e\2\2\u00a8\f\3\2\2\2\u00a9")
        buf.write("\u00aa\7v\2\2\u00aa\u00ab\7{\2\2\u00ab\u00ac\7r\2\2\u00ac")
        buf.write("\u00ad\7g\2\2\u00ad\16\3\2\2\2\u00ae\u00af\7u\2\2\u00af")
        buf.write("\u00b0\7v\2\2\u00b0\u00b1\7t\2\2\u00b1\u00b2\7w\2\2\u00b2")
        buf.write("\u00b3\7e\2\2\u00b3\u00b4\7v\2\2\u00b4\20\3\2\2\2\u00b5")
        buf.write("\u00b6\7k\2\2\u00b6\u00b7\7p\2\2\u00b7\u00b8\7v\2\2\u00b8")
        buf.write("\u00b9\7g\2\2\u00b9\u00ba\7t\2\2\u00ba\u00bb\7h\2\2\u00bb")
        buf.write("\u00bc\7c\2\2\u00bc\u00bd\7e\2\2\u00bd\u00be\7g\2\2\u00be")
        buf.write("\22\3\2\2\2\u00bf\u00c0\7u\2\2\u00c0\u00c1\7v\2\2\u00c1")
        buf.write("\u00c2\7t\2\2\u00c2\u00c3\7k\2\2\u00c3\u00c4\7p\2\2\u00c4")
        buf.write("\u00c9\7i\2\2\u00c5\u00c6\7u\2\2\u00c6\u00c7\7v\2\2\u00c7")
        buf.write("\u00c9\7t\2\2\u00c8\u00bf\3\2\2\2\u00c8\u00c5\3\2\2\2")
        buf.write("\u00c9\24\3\2\2\2\u00ca\u00cb\7k\2\2\u00cb\u00cc\7p\2")
        buf.write("\2\u00cc\u00cd\7v\2\2\u00cd\26\3\2\2\2\u00ce\u00cf\7h")
        buf.write("\2\2\u00cf\u00d0\7n\2\2\u00d0\u00d1\7q\2\2\u00d1\u00d2")
        buf.write("\7c\2\2\u00d2\u00d3\7v\2\2\u00d3\30\3\2\2\2\u00d4\u00d5")
        buf.write("\7d\2\2\u00d5\u00d6\7q\2\2\u00d6\u00d7\7q\2\2\u00d7\u00d8")
        buf.write("\7n\2\2\u00d8\u00d9\7g\2\2\u00d9\u00da\7c\2\2\u00da\u00db")
        buf.write("\7p\2\2\u00db\32\3\2\2\2\u00dc\u00dd\7e\2\2\u00dd\u00de")
        buf.write("\7q\2\2\u00de\u00df\7p\2\2\u00df\u00e0\7u\2\2\u00e0\u00e1")
        buf.write("\7v\2\2\u00e1\34\3\2\2\2\u00e2\u00e3\7x\2\2\u00e3\u00e4")
        buf.write("\7c\2\2\u00e4\u00e5\7t\2\2\u00e5\36\3\2\2\2\u00e6\u00e7")
        buf.write("\7e\2\2\u00e7\u00e8\7q\2\2\u00e8\u00e9\7p\2\2\u00e9\u00ea")
        buf.write("\7v\2\2\u00ea\u00eb\7k\2\2\u00eb\u00ec\7p\2\2\u00ec\u00ed")
        buf.write("\7w\2\2\u00ed\u00ee\7g\2\2\u00ee \3\2\2\2\u00ef\u00f0")
        buf.write("\7d\2\2\u00f0\u00f1\7t\2\2\u00f1\u00f2\7g\2\2\u00f2\u00f3")
        buf.write("\7c\2\2\u00f3\u00f4\7m\2\2\u00f4\"\3\2\2\2\u00f5\u00f6")
        buf.write("\7t\2\2\u00f6\u00f7\7c\2\2\u00f7\u00f8\7p\2\2\u00f8\u00f9")
        buf.write("\7i\2\2\u00f9\u00fa\7g\2\2\u00fa$\3\2\2\2\u00fb\u00fc")
        buf.write("\7p\2\2\u00fc\u00fd\7k\2\2\u00fd\u00fe\7n\2\2\u00fe&\3")
        buf.write("\2\2\2\u00ff\u0100\7v\2\2\u0100\u0101\7t\2\2\u0101\u0102")
        buf.write("\7w\2\2\u0102\u0103\7g\2\2\u0103(\3\2\2\2\u0104\u0105")
        buf.write("\7h\2\2\u0105\u0106\7c\2\2\u0106\u0107\7n\2\2\u0107\u0108")
        buf.write("\7u\2\2\u0108\u0109\7g\2\2\u0109*\3\2\2\2\u010a\u010b")
        buf.write("\7-\2\2\u010b,\3\2\2\2\u010c\u010d\7/\2\2\u010d.\3\2\2")
        buf.write("\2\u010e\u010f\7,\2\2\u010f\60\3\2\2\2\u0110\u0111\7\61")
        buf.write("\2\2\u0111\62\3\2\2\2\u0112\u0113\7\'\2\2\u0113\64\3\2")
        buf.write("\2\2\u0114\u0115\7?\2\2\u0115\u0116\7?\2\2\u0116\66\3")
        buf.write("\2\2\2\u0117\u0118\7#\2\2\u0118\u0119\7?\2\2\u01198\3")
        buf.write("\2\2\2\u011a\u011b\7>\2\2\u011b:\3\2\2\2\u011c\u011d\7")
        buf.write("@\2\2\u011d<\3\2\2\2\u011e\u011f\7>\2\2\u011f\u0120\7")
        buf.write("?\2\2\u0120>\3\2\2\2\u0121\u0122\7@\2\2\u0122\u0123\7")
        buf.write("?\2\2\u0123@\3\2\2\2\u0124\u0125\7?\2\2\u0125B\3\2\2\2")
        buf.write("\u0126\u0127\7,\2\2\u0127\u0128\7,\2\2\u0128D\3\2\2\2")
        buf.write("\u0129\u012a\7\60\2\2\u012aF\3\2\2\2\u012b\u012c\7<\2")
        buf.write("\2\u012c\u012d\7?\2\2\u012dH\3\2\2\2\u012e\u012f\7\61")
        buf.write("\2\2\u012f\u0130\7?\2\2\u0130J\3\2\2\2\u0131\u0132\7\'")
        buf.write("\2\2\u0132\u0133\7?\2\2\u0133L\3\2\2\2\u0134\u0135\7-")
        buf.write("\2\2\u0135\u0136\7?\2\2\u0136N\3\2\2\2\u0137\u0138\7/")
        buf.write("\2\2\u0138\u0139\7?\2\2\u0139P\3\2\2\2\u013a\u013b\7,")
        buf.write("\2\2\u013b\u013c\7?\2\2\u013cR\3\2\2\2\u013d\u013e\7#")
        buf.write("\2\2\u013eT\3\2\2\2\u013f\u0140\7~\2\2\u0140\u0141\7~")
        buf.write("\2\2\u0141V\3\2\2\2\u0142\u0143\7(\2\2\u0143\u0144\7(")
        buf.write("\2\2\u0144X\3\2\2\2\u0145\u0146\7]\2\2\u0146Z\3\2\2\2")
        buf.write("\u0147\u0148\7_\2\2\u0148\\\3\2\2\2\u0149\u014a\7*\2\2")
        buf.write("\u014a^\3\2\2\2\u014b\u014c\7+\2\2\u014c`\3\2\2\2\u014d")
        buf.write("\u014e\7.\2\2\u014eb\3\2\2\2\u014f\u0150\7}\2\2\u0150")
        buf.write("d\3\2\2\2\u0151\u0152\7\177\2\2\u0152f\3\2\2\2\u0153\u0154")
        buf.write("\7=\2\2\u0154h\3\2\2\2\u0155\u0156\7<\2\2\u0156j\3\2\2")
        buf.write("\2\u0157\u0158\5m\67\2\u0158l\3\2\2\2\u0159\u0162\7\62")
        buf.write("\2\2\u015a\u015e\t\2\2\2\u015b\u015d\t\3\2\2\u015c\u015b")
        buf.write("\3\2\2\2\u015d\u0160\3\2\2\2\u015e\u015c\3\2\2\2\u015e")
        buf.write("\u015f\3\2\2\2\u015f\u0162\3\2\2\2\u0160\u015e\3\2\2\2")
        buf.write("\u0161\u0159\3\2\2\2\u0161\u015a\3\2\2\2\u0162n\3\2\2")
        buf.write("\2\u0163\u0165\t\3\2\2\u0164\u0163\3\2\2\2\u0165\u0166")
        buf.write("\3\2\2\2\u0166\u0164\3\2\2\2\u0166\u0167\3\2\2\2\u0167")
        buf.write("\u0168\3\2\2\2\u0168\u016c\7\60\2\2\u0169\u016b\t\3\2")
        buf.write("\2\u016a\u0169\3\2\2\2\u016b\u016e\3\2\2\2\u016c\u016a")
        buf.write("\3\2\2\2\u016c\u016d\3\2\2\2\u016d\u0178\3\2\2\2\u016e")
        buf.write("\u016c\3\2\2\2\u016f\u0171\t\4\2\2\u0170\u0172\t\5\2\2")
        buf.write("\u0171\u0170\3\2\2\2\u0171\u0172\3\2\2\2\u0172\u0174\3")
        buf.write("\2\2\2\u0173\u0175\t\3\2\2\u0174\u0173\3\2\2\2\u0175\u0176")
        buf.write("\3\2\2\2\u0176\u0174\3\2\2\2\u0176\u0177\3\2\2\2\u0177")
        buf.write("\u0179\3\2\2\2\u0178\u016f\3\2\2\2\u0178\u0179\3\2\2\2")
        buf.write("\u0179p\3\2\2\2\u017a\u017b\7\62\2\2\u017b\u0180\t\6\2")
        buf.write("\2\u017c\u017e\7a\2\2\u017d\u017c\3\2\2\2\u017d\u017e")
        buf.write("\3\2\2\2\u017e\u017f\3\2\2\2\u017f\u0181\t\7\2\2\u0180")
        buf.write("\u017d\3\2\2\2\u0181\u0182\3\2\2\2\u0182\u0180\3\2\2\2")
        buf.write("\u0182\u0183\3\2\2\2\u0183r\3\2\2\2\u0184\u0185\7\62\2")
        buf.write("\2\u0185\u018a\t\b\2\2\u0186\u0188\7a\2\2\u0187\u0186")
        buf.write("\3\2\2\2\u0187\u0188\3\2\2\2\u0188\u0189\3\2\2\2\u0189")
        buf.write("\u018b\t\t\2\2\u018a\u0187\3\2\2\2\u018b\u018c\3\2\2\2")
        buf.write("\u018c\u018a\3\2\2\2\u018c\u018d\3\2\2\2\u018dt\3\2\2")
        buf.write("\2\u018e\u018f\7\62\2\2\u018f\u0194\t\n\2\2\u0190\u0192")
        buf.write("\7a\2\2\u0191\u0190\3\2\2\2\u0191\u0192\3\2\2\2\u0192")
        buf.write("\u0193\3\2\2\2\u0193\u0195\t\13\2\2\u0194\u0191\3\2\2")
        buf.write("\2\u0195\u0196\3\2\2\2\u0196\u0194\3\2\2\2\u0196\u0197")
        buf.write("\3\2\2\2\u0197v\3\2\2\2\u0198\u019b\5\'\24\2\u0199\u019b")
        buf.write("\5)\25\2\u019a\u0198\3\2\2\2\u019a\u0199\3\2\2\2\u019b")
        buf.write("x\3\2\2\2\u019c\u01a0\t\f\2\2\u019d\u019f\t\r\2\2\u019e")
        buf.write("\u019d\3\2\2\2\u019f\u01a2\3\2\2\2\u01a0\u019e\3\2\2\2")
        buf.write("\u01a0\u01a1\3\2\2\2\u01a1z\3\2\2\2\u01a2\u01a0\3\2\2")
        buf.write("\2\u01a3\u01a7\7$\2\2\u01a4\u01a6\5}?\2\u01a5\u01a4\3")
        buf.write("\2\2\2\u01a6\u01a9\3\2\2\2\u01a7\u01a5\3\2\2\2\u01a7\u01a8")
        buf.write("\3\2\2\2\u01a8\u01aa\3\2\2\2\u01a9\u01a7\3\2\2\2\u01aa")
        buf.write("\u01ab\7$\2\2\u01ab|\3\2\2\2\u01ac\u01af\n\16\2\2\u01ad")
        buf.write("\u01af\5\177@\2\u01ae\u01ac\3\2\2\2\u01ae\u01ad\3\2\2")
        buf.write("\2\u01af~\3\2\2\2\u01b0\u01b1\7^\2\2\u01b1\u01b5\t\17")
        buf.write("\2\2\u01b2\u01b3\7^\2\2\u01b3\u01b5\7$\2\2\u01b4\u01b0")
        buf.write("\3\2\2\2\u01b4\u01b2\3\2\2\2\u01b5\u0080\3\2\2\2\u01b6")
        buf.write("\u01ba\t\20\2\2\u01b7\u01b8\7^\2\2\u01b8\u01ba\n\21\2")
        buf.write("\2\u01b9\u01b6\3\2\2\2\u01b9\u01b7\3\2\2\2\u01ba\u0082")
        buf.write("\3\2\2\2\u01bb\u01bc\7\61\2\2\u01bc\u01bd\7\61\2\2\u01bd")
        buf.write("\u01c1\3\2\2\2\u01be\u01c0\n\22\2\2\u01bf\u01be\3\2\2")
        buf.write("\2\u01c0\u01c3\3\2\2\2\u01c1\u01bf\3\2\2\2\u01c1\u01c2")
        buf.write("\3\2\2\2\u01c2\u01c4\3\2\2\2\u01c3\u01c1\3\2\2\2\u01c4")
        buf.write("\u01c5\bB\2\2\u01c5\u0084\3\2\2\2\u01c6\u01c7\7\61\2\2")
        buf.write("\u01c7\u01c8\7,\2\2\u01c8\u01cd\3\2\2\2\u01c9\u01cc\5")
        buf.write("\u0085C\2\u01ca\u01cc\13\2\2\2\u01cb\u01c9\3\2\2\2\u01cb")
        buf.write("\u01ca\3\2\2\2\u01cc\u01cf\3\2\2\2\u01cd\u01ce\3\2\2\2")
        buf.write("\u01cd\u01cb\3\2\2\2\u01ce\u01d0\3\2\2\2\u01cf\u01cd\3")
        buf.write("\2\2\2\u01d0\u01d1\7,\2\2\u01d1\u01d2\7\61\2\2\u01d2\u01d3")
        buf.write("\3\2\2\2\u01d3\u01d4\bC\2\2\u01d4\u0086\3\2\2\2\u01d5")
        buf.write("\u01d7\7\17\2\2\u01d6\u01d5\3\2\2\2\u01d6\u01d7\3\2\2")
        buf.write("\2\u01d7\u01d8\3\2\2\2\u01d8\u01d9\7\f\2\2\u01d9\u01da")
        buf.write("\bD\3\2\u01da\u0088\3\2\2\2\u01db\u01dd\t\23\2\2\u01dc")
        buf.write("\u01db\3\2\2\2\u01dd\u01de\3\2\2\2\u01de\u01dc\3\2\2\2")
        buf.write("\u01de\u01df\3\2\2\2\u01df\u01e0\3\2\2\2\u01e0\u01e1\b")
        buf.write("E\2\2\u01e1\u008a\3\2\2\2\u01e2\u01e3\13\2\2\2\u01e3\u01e4")
        buf.write("\bF\4\2\u01e4\u008c\3\2\2\2\u01e5\u01eb\7$\2\2\u01e6\u01ea")
        buf.write("\n\24\2\2\u01e7\u01e8\7^\2\2\u01e8\u01ea\t\25\2\2\u01e9")
        buf.write("\u01e6\3\2\2\2\u01e9\u01e7\3\2\2\2\u01ea\u01ed\3\2\2\2")
        buf.write("\u01eb\u01e9\3\2\2\2\u01eb\u01ec\3\2\2\2\u01ec\u01ef\3")
        buf.write("\2\2\2\u01ed\u01eb\3\2\2\2\u01ee\u01f0\t\26\2\2\u01ef")
        buf.write("\u01ee\3\2\2\2\u01f0\u01f1\3\2\2\2\u01f1\u01f2\bG\5\2")
        buf.write("\u01f2\u008e\3\2\2\2\u01f3\u01f7\7$\2\2\u01f4\u01f6\5")
        buf.write("}?\2\u01f5\u01f4\3\2\2\2\u01f6\u01f9\3\2\2\2\u01f7\u01f5")
        buf.write("\3\2\2\2\u01f7\u01f8\3\2\2\2\u01f8\u01fa\3\2\2\2\u01f9")
        buf.write("\u01f7\3\2\2\2\u01fa\u01fb\5\u0081A\2\u01fb\u01fc\bH\6")
        buf.write("\2\u01fc\u0090\3\2\2\2 \2\u00c8\u015e\u0161\u0166\u016c")
        buf.write("\u0171\u0176\u0178\u017d\u0182\u0187\u018c\u0191\u0196")
        buf.write("\u019a\u01a0\u01a7\u01ae\u01b4\u01b9\u01c1\u01cb\u01cd")
        buf.write("\u01d6\u01de\u01e9\u01eb\u01ef\u01f7\7\b\2\2\3D\2\3F\3")
        buf.write("\3G\4\3H\5")
        return buf.getvalue()


class MiniGoLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    IF = 1
    ELSE = 2
    FOR = 3
    RETURN = 4
    FUNC = 5
    TYPE = 6
    STRUCT = 7
    INTERFACE = 8
    STRING = 9
    INT = 10
    FLOAT = 11
    BOOLEAN = 12
    CONST = 13
    VAR = 14
    CONTINUE = 15
    BREAK = 16
    RANGE = 17
    NIL = 18
    TRUE = 19
    FALSE = 20
    ADD = 21
    SUB = 22
    MUL = 23
    DIV = 24
    MOD = 25
    EQ = 26
    NEQ = 27
    LT = 28
    GT = 29
    LTE = 30
    GTE = 31
    ASSIGNINIT = 32
    EXP = 33
    DOT = 34
    ASSIGN = 35
    E_DIV = 36
    E_MOD = 37
    E_ADD = 38
    E_SUB = 39
    E_MUL = 40
    NOT = 41
    OR = 42
    AND = 43
    LSB = 44
    RSB = 45
    LP = 46
    RP = 47
    CM = 48
    LCB = 49
    RCB = 50
    SC = 51
    CO = 52
    INT_LIT = 53
    FLOAT_LIT = 54
    HEX_LIT = 55
    BI_LIT = 56
    OCT_LIT = 57
    BOOL_LIT = 58
    ID = 59
    STRING_LIT = 60
    COMMENT_LINE = 61
    COMMENT = 62
    NEWLINE = 63
    WS = 64
    ERROR_CHAR = 65
    UNCLOSE_STRING = 66
    ILLEGAL_ESCAPE = 67

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'if'", "'else'", "'for'", "'return'", "'func'", "'type'", "'struct'", 
            "'interface'", "'int'", "'float'", "'boolean'", "'const'", "'var'", 
            "'continue'", "'break'", "'range'", "'nil'", "'true'", "'false'", 
            "'+'", "'-'", "'*'", "'/'", "'%'", "'=='", "'!='", "'<'", "'>'", 
            "'<='", "'>='", "'='", "'**'", "'.'", "':='", "'/='", "'%='", 
            "'+='", "'-='", "'*='", "'!'", "'||'", "'&&'", "'['", "']'", 
            "'('", "')'", "','", "'{'", "'}'", "';'", "':'" ]

    symbolicNames = [ "<INVALID>",
            "IF", "ELSE", "FOR", "RETURN", "FUNC", "TYPE", "STRUCT", "INTERFACE", 
            "STRING", "INT", "FLOAT", "BOOLEAN", "CONST", "VAR", "CONTINUE", 
            "BREAK", "RANGE", "NIL", "TRUE", "FALSE", "ADD", "SUB", "MUL", 
            "DIV", "MOD", "EQ", "NEQ", "LT", "GT", "LTE", "GTE", "ASSIGNINIT", 
            "EXP", "DOT", "ASSIGN", "E_DIV", "E_MOD", "E_ADD", "E_SUB", 
            "E_MUL", "NOT", "OR", "AND", "LSB", "RSB", "LP", "RP", "CM", 
            "LCB", "RCB", "SC", "CO", "INT_LIT", "FLOAT_LIT", "HEX_LIT", 
            "BI_LIT", "OCT_LIT", "BOOL_LIT", "ID", "STRING_LIT", "COMMENT_LINE", 
            "COMMENT", "NEWLINE", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
            "ILLEGAL_ESCAPE" ]

    ruleNames = [ "IF", "ELSE", "FOR", "RETURN", "FUNC", "TYPE", "STRUCT", 
                  "INTERFACE", "STRING", "INT", "FLOAT", "BOOLEAN", "CONST", 
                  "VAR", "CONTINUE", "BREAK", "RANGE", "NIL", "TRUE", "FALSE", 
                  "ADD", "SUB", "MUL", "DIV", "MOD", "EQ", "NEQ", "LT", 
                  "GT", "LTE", "GTE", "ASSIGNINIT", "EXP", "DOT", "ASSIGN", 
                  "E_DIV", "E_MOD", "E_ADD", "E_SUB", "E_MUL", "NOT", "OR", 
                  "AND", "LSB", "RSB", "LP", "RP", "CM", "LCB", "RCB", "SC", 
                  "CO", "INT_LIT", "Int", "FLOAT_LIT", "HEX_LIT", "BI_LIT", 
                  "OCT_LIT", "BOOL_LIT", "ID", "STRING_LIT", "STR_CHAR", 
                  "ESC_SEQ", "ESC_ILLEGAL", "COMMENT_LINE", "COMMENT", "NEWLINE", 
                  "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    grammarFileName = "MiniGo.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    from antlr4.Token import Token
    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None
        self.preType = None

    def emit(self):
        tk = self.type
        self.preType = tk;
        if tk == self.UNCLOSE_STRING:       
            result = super().emit();
            raise UncloseString(result.text);
        elif tk == self.ILLEGAL_ESCAPE:
            result = super().emit();
            raise IllegalEscape(result.text);
        elif tk == self.ERROR_CHAR:
            result = super().emit();
            raise ErrorToken(result.text); 
        else:
            return super().emit();

    def insertSemicolon(self):
        prev = self.preType
        #if(prev!=None):
            #print(self.symbolicNames[prev])
        if(prev==None):
            self.skip()
        elif(prev in [
                self.INT_LIT, self.ID, self.FLOAT_LIT, self.OCT_LIT, self.HEX_LIT,
                self.BI_LIT, self.STRING_LIT, self.RETURN, self.CONTINUE, self.BREAK,
                self.TRUE,self.FALSE, self.RCB, self.RP, self.RSB, self.NIL
            ]):
            self.text = ';'
        else:
            self.skip()



    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[66] = self.NEWLINE_action 
            actions[68] = self.ERROR_CHAR_action 
            actions[69] = self.UNCLOSE_STRING_action 
            actions[70] = self.ILLEGAL_ESCAPE_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def NEWLINE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.insertSemicolon()
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            raise ErrorToken(self.text)
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

                if (len(self.text) >= 3 and self.text[-1] == '\n' and self.text[-2] == '\r'):
                    raise UncloseString(self.text[0:-2])
                elif self.text[-1] == '\n':
                    raise UncloseString(self.text[:-1])
                else:
                    raise UncloseString(self.text)

     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:
             raise IllegalEscape(self.text); 
     


