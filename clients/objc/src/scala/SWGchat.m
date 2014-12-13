#import "SWGDate.h"
#import "SWGChat.h"

@implementation SWGChat

-(id)date: (SWGDate*) date
    user: (NSString*) user
    message: (NSString*) message
    html: (NSString*) html
    fromBot: (NSNumber*) fromBot
    _id: (NSNumber*) _id
{
  _date = date;
  _user = user;
  _message = message;
  _html = html;
  _fromBot = fromBot;
  __id = _id;
  return self;
}

-(id) initWithValues:(NSDictionary*)dict
{
    self = [super init];
    if(self) {
        id date_dict = dict[@"date"];
        if(date_dict != nil)
            _date = [[SWGDate alloc]initWithValues:date_dict];
        _user = dict[@"user"]; 
        _message = dict[@"message"]; 
        _html = dict[@"html"]; 
        _fromBot = dict[@"fromBot"]; 
        __id = dict[@"id"]; 
        

    }
    return self;
}

-(NSDictionary*) asDictionary {
    NSMutableDictionary* dict = [[NSMutableDictionary alloc] init];
    if(_date != nil){
        if([_date isKindOfClass:[NSArray class]]){
            NSMutableArray * array = [[NSMutableArray alloc] init];
            for( SWGDate *date in (NSArray*)_date) {
                [array addObject:[(SWGObject*)date asDictionary]];
            }
            dict[@"date"] = array;
        }
        else if(_date && [_date isKindOfClass:[SWGDate class]]) {
            NSString * dateString = [(SWGDate*)_date toString];
            if(dateString){
                dict[@"date"] = dateString;
            }
        }
        else {
        if(_date != nil) dict[@"date"] = [(SWGObject*)_date asDictionary];
        }
    }
    if(_user != nil) dict[@"user"] = _user ;
        if(_message != nil) dict[@"message"] = _message ;
        if(_html != nil) dict[@"html"] = _html ;
        if(_fromBot != nil) dict[@"fromBot"] = _fromBot ;
        if(__id != nil) dict[@"id"] = __id ;
        NSDictionary* output = [dict copy];
    return output;
}

@end

