public class GenerateCity
{
    
    private String gender;
    private String name;
    private Dictionary<string, string> id;

    public GenerateCity (String gender) {
        string[] world = { 'above ground','under ground','city centre','slums','eco dome','space shuttle station','trade center' };
        string[] size = { 'tiny','small','medium','large','huge' };
        string[] place = { 'castle','hold','city','town','village','camp' };
        string[] residence = { 'road','street','avenue','alley','path','circle','square' };
        string[] place_desc = { 'high','remote','exposed','small','broken','diverse','rough','dark','shadowy','contested','grim','wild','fertile','blocked','ancient','perilous','hidden','occupied','rich','big','savage','defended','withered','mystical','inaccessible','protected','abandoned','wide','foul','dead','ruined','barren','cold','blighted','low','beautiful','abundant','lush','flooded','empty','strange','corrupted','peaceful','forgotten','expansive','settled','dense','civilized','desolate','isolated' };
        
        this.id = {
            world: "",
            size: "",
            place: "",
            residence: "",
            place_desc: "",
        };

        var rand = new Random();

        this.id["world"] = this.world[rand]
        this.id["size"] = this.size[rand]
        this.id["place"] = this.place[rand]
        this.id["residence"] = this.residence[rand]
        this.id["place_desc"] = this.place_desc[rand]
    }

    public getId() {
        return this.id;
    }
}
